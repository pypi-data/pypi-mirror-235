import copy
import time
import heapq
import traceback
import threading

from prometheus_client import Gauge, Counter, Histogram

_collected_total = Counter(
    "httpsd_garbage_collection_collected_items_total",
    "The total count of the garbage collection collected items.",
    ["name"],
)

_thread_cache_count = Gauge(
    "httpsd_garbage_collection_cache_count",
    "Show current thread_cache count",
    ["name"],
)

_heap_cache_count = Gauge(
    "httpsd_garbage_collection_heap_count",
    "Show current heap length",
    ["name"],
)

_collection_run_interval = Histogram(
    "http_sd_garbage_collection_run_interval_seconds_bucket",
    "The interval of two garbage collection run.",
    ["name"],
)


class CachedScriptException(Exception):
    """Raised when user's function raises an exception."""

    def __init__(self, message, exception_type="Exception", traceback=[]):
        traceback = "".join(traceback)
        super().__init__(
            self,
            f"""this is a cached exception,
type: {exception_type}, message: {message}, traceback: {traceback}""",
        )


class TimeoutException(Exception):
    """Raised when target function timeout."""

    pass


class TimeoutDecorator:
    def __init__(
        self,
        timeout=None,
        cache_time=0,
        cache_exception_time=0,
        name="",
        garbage_collection_interval=5,
        garbage_collection_count=30,
        copy_response=False,
    ):
        """
        Use threading and cache to store the function result.

        Garbage Collection time complexity:
            worse: O(nlogn)
            average in every operation: O(logn)

        Parameters
        ----------
        timeout: int
            function timeout. if exceed, raise TimeoutException (in sec).
        cache_time: int
            after function return normally,
                how long should we cache the result (in sec).
        cache_exception_time: int
            after function return incorrectly,
                how long should we cache the exception (in sec).
        name: str
            prometheus_client metrics prefix
        garbage_collection_count: int
            garbage collection threshold
        garbage_collection_interval: int
            the second to avoid collection too often.
        copy_response: bool
            use copy.deepcopy on the response from the target function.

        Returns
        -------
        TimeoutDecorator
            decorator class.
        """
        self.timeout = timeout
        self.cache_time = cache_time
        self.cache_exception_time = cache_exception_time
        self.name = name
        self.garbage_collection_interval = garbage_collection_interval
        self.garbage_collection_count = garbage_collection_count
        self.copy_response = copy_response

        self.thread_cache = {}
        self.cache_lock = threading.Lock()
        self.heap = []
        self.heap_lock = threading.Lock()
        self.garbage_collection_timestamp = 0
        self.garbage_collection_lock = threading.Lock()

    def can_garbage_collection(self):
        """Check current state can run garbage collection."""
        return (
            self.garbage_collection_interval
            + self.garbage_collection_timestamp
            < time.time()
            and len(self.heap) > self.garbage_collection_count
        )

    def _cache_garbage_collection(self):
        def can_iterate():
            with self.heap_lock:
                if len(self.heap) == 0 or self.heap[0][0] > time.time():
                    return False
            return True

        worked_keys = {}
        while can_iterate():
            _timestamp, _key = None, None
            with self.heap_lock:
                _timestamp, _key = heapq.heappop(self.heap)
            if _key in worked_keys:
                continue
            worked_keys[_key] = True
            with self.cache_lock:
                if _key not in self.thread_cache:
                    continue
                if self.is_expired(self.thread_cache[_key]):
                    if "traceback" in self.thread_cache[_key]:
                        traceback.clear_frames(
                            self.thread_cache[_key]["traceback"],
                        )
                    del self.thread_cache[_key]
                    _collected_total.labels(name=self.name).inc(1)
        _heap_cache_count.labels(
            name=self.name,
        ).set(len(self.heap))
        _thread_cache_count.labels(
            name=self.name,
        ).set(len(self.thread_cache))
        current_time = time.time()
        if self.garbage_collection_timestamp != 0:
            _collection_run_interval.labels(
                name=self.name,
            ).observe(current_time - self.garbage_collection_timestamp)
        self.garbage_collection_timestamp = current_time

    def is_expired(self, cache):
        """Check thread_cache dict is expired."""
        return cache["expired_timestamp"] < time.time()

    def _cal_cache_key(*arg, **kwargs):
        return hash(tuple([hash(arg), tuple(sorted(kwargs.items()))]))

    def __call__(self, function):
        def wrapper(*arg, **kwargs):
            cache = {
                "thread": None,
                "error": None,
                "response": None,
                "expired_timestamp": float("inf"),
            }

            def target_function(key):
                try:
                    if self.copy_response:
                        cache["response"] = copy.deepcopy(
                            function(*arg, **kwargs),
                        )
                    else:
                        cache["response"] = function(*arg, **kwargs)
                    cache["expired_timestamp"] = time.time() + self.cache_time
                except Exception as e:
                    cache["error"] = {
                        "message": str(e),
                        "error_type": type(e).__name__,
                        "traceback": e.__traceback__,
                    }
                    cache["expired_timestamp"] = (
                        time.time() + self.cache_exception_time
                    )
                with self.heap_lock:
                    heapq.heappush(
                        self.heap,
                        (
                            cache["expired_timestamp"],
                            key,
                        ),
                    )
                    _heap_cache_count.labels(
                        name=self.name,
                    ).set(len(self.heap))

            key = self._cal_cache_key(*arg, **kwargs)
            with self.cache_lock:
                if key in self.thread_cache:
                    if self.thread_cache[key][
                        "thread"
                    ].is_alive() or not self.is_expired(
                        self.thread_cache[key]
                    ):
                        cache = self.thread_cache[key]
                if cache["thread"] is None:
                    cache["thread"] = threading.Thread(
                        target=target_function,
                        args=(key,),
                    )
                    cache["thread"].start()
                self.thread_cache[key] = cache
                _thread_cache_count.labels(
                    name=self.name,
                ).set(len(self.thread_cache))
            cache["thread"].join(self.timeout)

            if (
                self.can_garbage_collection()
                and self.garbage_collection_lock.acquire(False)
            ):
                try:
                    self._cache_garbage_collection()
                finally:
                    self.garbage_collection_lock.release()
            if cache["thread"].is_alive():
                raise TimeoutException("target function timeout!")
            if cache["error"]:
                e = cache["error"]
                # avoid duplicated append the traceback
                raise CachedScriptException(
                    e["message"],
                    e["error_type"],
                    traceback.format_tb(e["traceback"]),
                ).with_traceback(e["traceback"])
            return copy.deepcopy(cache["response"])

        return wrapper
