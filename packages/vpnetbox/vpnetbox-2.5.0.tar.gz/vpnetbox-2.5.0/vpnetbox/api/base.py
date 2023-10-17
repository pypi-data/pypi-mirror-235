"""Base methods for Aggregates, Prefixes, Addresses."""

from __future__ import annotations

import json
import logging
import re
import time
from abc import ABC, abstractmethod
from operator import itemgetter
from queue import Queue
from threading import Thread
from typing import Any, Iterable, Tuple
from urllib.parse import urlencode

import requests
from requests import Session, Response
from requests.exceptions import ReadTimeout, ConnectionError as RequestsConnectionError

from vpnetbox import helpers as h
from vpnetbox.api.exceptions import NbApiError
from vpnetbox.types_ import DAny, DStr, SeStr, UParam, LDAny, LValue, LTInt2, LParam, SStr, TStr
from vpnetbox.types_ import TLists, TValues

LIMIT = 1000  # max items limit in response


class Base(ABC):
    """Base methods for Aggregates, Prefixes, Addresses."""

    _reserved_ipam_keys = [
        "overlapped",
        "warnings",
        "nbnets",
        "nbnets__subnets",
    ]

    def __init__(self, **kwargs):
        """Init Base.

        :param host: Netbox host name.
        :type host: str

        :param token: Netbox token.
        :type token: str

        :param verify: True - TLS certificate required,
                       False - Requests will accept any TLS certificate.
        :type verify: bool

        :param limit: Split the query to multiple requests if the response exceeds the limit.
            Default 1000.
        :type limit: int

        :param threads: Threads count. Default 1, loop mode.
        :type threads: int

        :param interval: Wait this time between requests (seconds).
            Default 0. Useful for request speed shaping.
        :type interval: int

        :param max_items: Stop the request if received items reach this value.
            Default unlimited. Useful if you need many objects but not all.
        :type max_items: int

        :param timeout: Request timeout (seconds). Default 60.
        :type timeout: float

        :param max_retries: Retry the request multiple times if it receives a 500 error
            or timed-out. Default 3.
        :type max_retries: int

        :param sleep: Interval before the next retry after receiving a 500 error (seconds).
            Default 10.
        :type sleep: float

        :param url_max_len: Split the query to multiple requests if the URL length exceeds
            this value. Default ~3900.
        :type url_max_len: int
        """
        self.host: str = str(kwargs.get("host") or "")
        self.token: str = str(kwargs.get("token") or "")
        self.url: str = f"https://{self.host}"

        self.verify: bool = self._init_verify(**kwargs)
        self.limit: int = int(kwargs.get("limit") or LIMIT)
        self.max_items: int = int(kwargs.get("max_items") or 0)
        self.timeout: float = float(kwargs.get("timeout") or 60)
        self.max_retries: int = int(kwargs.get("max_retries") or 3)
        self.sleep: float = float(kwargs.get("sleep") or 10)
        self.calls_interval: float = float(kwargs.get("sleep") or 0)
        self.threads: int = _init_threads(**kwargs)
        self.interval: int = int(kwargs.get("interval") or 0)
        self.url_max_len = int(kwargs.get("url_max_len") or 3900)

        self._session = self._init_session()
        self.default: DAny = {}  # default params
        self._query = ""  # "ipam/ip-addresses/", etc.
        self._sliced = ""  # "address", "_"
        self._concurrent: TStr = tuple()  # concurrent params
        self._results: LDAny = []  # storage for received objects from Netbox

    def __repr__(self) -> str:
        """__repr__."""
        name = self.__class__.__name__
        return f"<{name}: {self.host}>"

    # ============================= init =============================

    @staticmethod
    def _init_session() -> Session:
        """Init session. Required for unittests."""
        return requests.session()

    @staticmethod
    def _init_verify(**kwargs) -> bool:
        """Init verify. False - Requests will accept any TLS certificate."""
        verify = kwargs.get("verify")
        if verify is None:
            return True
        return bool(verify)

    # =========================== method =============================

    def create(self, data: DAny) -> Response:
        """Create object in Netbox.

        :param data: Data of new object.
        :return: Session response.
            *<Response [201]>* Object successfully created,
            *<Response [400]>* Object already exist.
        """
        kwargs = dict(url=f"{self.url}/api/{self._query}",
                      headers=self._headers(),
                      data=json.dumps(data),
                      verify=self.verify,
                      timeout=self.timeout)
        return self._session.post(**kwargs)

    # noinspection PyShadowingBuiltins
    def delete(self, id: int) -> Response:  # pylint: disable=redefined-builtin
        """Delete object in Netbox.

        :param id: Unique identifier.
        :return: Session response. *<Response [204]>* Object successfully deleted.
        """
        kwargs = dict(url=f"{self.url}/api/{self._query}{id}",
                      headers=self._headers(),
                      verify=self.verify,
                      timeout=self.timeout)
        return self._session.delete(**kwargs)

    @abstractmethod
    def get(self, **kwargs) -> LDAny:
        """Get data from Netbox."""

    def query(self, query: str, params: UParam = None) -> LDAny:
        """Retrieve data from Netbox.

        :param query: Query string.
        :param params: Parameters to request from Netbox.
        :return: A list of the Netbox objects.
        :example:
            query(query="ipam/ip-addresses/", params=[("status", "active")]) ->
            [{"id": 1, "address": "", ...}, ...]
        """
        if params is None:
            params = []
        params_d = h.params_to_dict(params)
        return self._query_loop_offset(query, params_d)

    def query_count(self, params: LParam) -> int:
        """Get count of Netbox objects."""
        response: Response = self._session.get(
            url=f"{self.url}/api/{self._query}?{urlencode(params)}",
            headers=self._headers(),
            verify=self.verify,
            timeout=self.timeout,
        )
        if not response.ok:
            return 0
        html: str = response.content.decode("utf-8")
        count = int(json.loads(html)["count"])
        return count

    # noinspection PyShadowingBuiltins
    def update(self, id: int, data: DAny) -> Response:  # pylint: disable=redefined-builtin
        """Update object in Netbox.

        :param id: Unique identifier.
        :param data: New data.
        :return: Session response. *<Response [200]>* Object successfully updated.
        """
        kwargs = dict(url=f"{self.url}/api/{self._query}{id}/",
                      headers=self._headers(),
                      data=json.dumps(data),
                      verify=self.verify,
                      timeout=self.timeout)
        return self._session.patch(**kwargs)

    def version(self) -> str:
        """Get Netbox version.

        :return: Netbox version if >=3.* else "".
        """
        url = f"{self.url}/api/status/"
        headers = self._headers()
        kwargs = dict(url=url, headers=headers, verify=self.verify, timeout=self.timeout)
        response: Response = self._session.get(**kwargs)

        # Netbox version < 3.x.x
        if self._is_status_code_400(response):
            return ""

        # Netbox version >= 3.x.x
        if response.ok:
            html: str = response.content.decode("utf-8")
            result: DAny = json.loads(html)
            version = result.get("netbox-version") or ""
            return version

        # error
        msg = self._msg_status_code(response)
        raise ConnectionError(f"Netbox server error: {msg}")

    # ============================== query ===============================

    def _query_params_ld(self, params: LDAny) -> LDAny:
        """Retrieve data from Netbox.

        :param params: Parameters to request from Netbox.
        :return: A list of the Netbox objects.
        """
        # slicing params for long URL
        params_: LDAny = []
        for params_d in params:
            if self._sliced in params_d:
                params_sliced: LDAny = self._slice_params(params_d)
                params_.extend(params_sliced)
            else:
                params_.append(params_d)

        # query
        self._results = []
        if self.threads > 1:
            results_count: LDAny = self._query_threads_count(params_)
            params_ = self._slice_params_counters(results_count)
            self._query_threads(method=self._query_data_thread, params=params_)
        else:
            for params_d in params_:
                results_: LDAny = self._query_loop_offset(self._query, params_d)
                self._results.extend(results_)

        results: LDAny = sorted(self._results, key=itemgetter("id"))
        results = h.no_dupl(results)
        self._results = []
        return results

    def _query_count(self, query: str, params_d: DAny) -> None:
        """Retrieve counters of interested objects from Netbox.

        :param query: Query string.
        :param params_d: Parameters to request from Netbox.
        :return: None. Update self object.
        """
        params_d_ = params_d.copy()
        params_d_["brief"] = 1
        params_d_["limit"] = 1
        params_l: LParam = h.dict_to_params(params_d_)
        url = f"{self.url}/api/{query}?{urlencode(params_l)}"
        response: Response = self._retry_requests(url)

        count = 0
        if response.ok:
            html: str = response.content.decode("utf-8")
            data: DAny = json.loads(html)
            count = int(data["count"])

        result = {"count": count, "params_d": params_d}
        self._results.append(result)

    def _query_loop_offset(self, query: str, params_d: DAny) -> LDAny:
        """Retrieve data from Netbox.

        If the number of items in the result exceeds the limit, iterate through the offset
        in a loop mode.

        :param query: Query string.
        :param params_d: Parameters to request from Netbox.
        :return: Netbox objects. Update self _results.
        """
        if not params_d.get("limit"):
            params_d["limit"] = self.limit
        params_l: LParam = h.dict_to_params(params_d)
        offset = 0

        results: LDAny = []
        while True:
            params_i = [*params_l, ("offset", offset)]
            url = f"{self.url}/api/{query}?{urlencode(params_i)}"
            response: Response = self._retry_requests(url)
            if response.ok:
                html: str = response.content.decode("utf-8")
                data: DAny = json.loads(html)
                results_: LDAny = list(data["results"])
                results.extend(results_)
            else:
                results_ = []

            # stop requests if limit reached
            if self.limit != len(results_):
                break
            if self.max_items and self.max_items <= len(results):
                break

            # next iteration
            if self.interval:
                time.sleep(self.interval)
            offset += self.limit

        return results

    def _query_data_thread(self, query: str, params_d: DAny) -> None:
        """Retrieve data from Netbox.

        If the number of items in the result exceeds the limit, iterate through the offset
        in a loop mode.
        :param query: Query string.
        :param params_d: Parameters to request from Netbox.
        :return: Netbox objects. Update self _results.
        """
        params_l: LParam = h.dict_to_params(params_d)
        url = f"{self.url}/api/{query}?{urlencode(params_l)}"
        response: Response = self._retry_requests(url)
        if response.ok:
            html: str = response.content.decode("utf-8")
            data: DAny = json.loads(html)
            results_: LDAny = list(data["results"])
            self._results.extend(results_)

    def _query_threads_count(self, params: LDAny) -> LDAny:
        """Retrieve counters of interested objects from Netbox in threaded mode.

        :param params: Parameters to request from Netbox.
        :return: List of dict with counters and parameters of interested objects.
        """
        self._results = []
        self._query_threads(method=self._query_count, params=params)
        results: LDAny = self._results
        self._results = []
        return results

    def _query_threads(self, method: callable, params: LDAny) -> None:
        """Retrieve data from Netbox in threaded mode.

        :param method: Method that need call with parameters.
        :param params: Parameters to request from Netbox.
        :return: None. Save results to self._results.
        """
        queue = Queue()
        for params_d in params:
            queue.put((method, params_d))

        for idx in range(self.threads):
            if self.interval:
                time.sleep(self.interval)
            thread = Thread(name=f"Thread-{idx}", target=self._run_queue, args=(queue,))
            thread.start()
        queue.join()

    def _run_queue(self, queue: Queue) -> None:
        """Process tasks from the queue.

        This method dequeues and executes tasks until the queue is empty.
        Each task is expected to be a callable method with its corresponding params_d parameters.
        :param queue: A queue containing (method, params_d) pairs to be executed.
        """
        while not queue.empty():
            method, params_d = queue.get()
            method(self._query, params_d)
            queue.task_done()

    def _retry_requests(self, url: str) -> Response:
        """Retry multiple requests if session is timed out or error."""
        counter = 0
        while counter < self.max_retries:
            counter += 1

            try:
                response: Response = self._session.get(
                    url=url,
                    headers=self._headers(),
                    verify=self.verify,
                    timeout=self.timeout,
                )
            except ReadTimeout:
                attempts = f"{counter} of {self.max_retries}"
                msg = f"Session timeout={self.timeout!r}sec reached, {attempts=}."
                logging.warning(msg)
                if counter < self.max_retries:
                    msg = f"Next attempt after sleep={self.sleep}sec."
                    logging.warning(msg)
                    time.sleep(self.sleep)
                continue
            except RequestsConnectionError as ex:
                raise ConnectionError(f"Netbox connection error: {ex}") from ex

            if response.ok:
                return response
            msg = self._msg_status_code(response)
            msg.lstrip(".")
            if self._is_status_code_500(response):
                raise ConnectionError(f"Netbox server error: {msg}.")
            if self._is_credentials_error(response):
                raise ConnectionError(f"Netbox credentials error: {msg}.")
            if self._is_not_available_error(response):
                logging.warning(msg)
                return response
            raise ConnectionError(f"ConnectionError: {msg}.")

        msg = f"max_retries={self.max_retries!r} reached."
        logging.warning(msg)
        response = Response()
        response.status_code = 504  # Gateway Timeout
        response._content = str.encode(msg)
        return response

    # ============================== helper ==============================

    def _headers(self) -> DStr:
        """Return session headers."""
        headers = {"Authorization": f"Token {self.token}",
                   "Content-Type": "application/json"}
        return headers

    def _add_default_to_params(self, *params) -> LDAny:
        """Add default params."""
        if not params:
            return [self.default.copy()]
        params_: LDAny = []
        for params_d in params:
            keys = sorted(list(self.default), reverse=True)
            for key in keys:
                if params_d.get(key) is None:
                    params_d = {**{key: self.default[key]}, **params_d}

            params_.append(params_d)
        return params_

    @staticmethod
    def _format_rse_upper_lower(items: LDAny) -> None:
        """Update items, sets upper/lower-case for role, site, env."""
        for data in items:
            if role := data.get("role", {}):
                if slug := role.get("slug", ""):
                    data["role"]["slug"] = slug.upper()
            if site := data.get("site", {}):
                if name := site.get("name", ""):
                    data["site"]["name"] = name.lower()
            if custom_field := data.get("custom_field", {}):
                if env := custom_field.get("env", ""):
                    data["custom_field"]["env"] = env.upper()

    def _params_sliced(self, params_d: DAny) -> Tuple[LParam, DAny]:
        """Slice the parameters based on the given sliced key.

        :param params_d: The dictionary ot the parameters.
        :return: A tuple containing the sliced parameters and a dictionary of the sliced
            key-value pairs.
        """
        params: LParam = []
        sliced_d: DAny = {}
        for key, value in params_d.items():
            if key == self._sliced:
                sliced_d[key] = value
                continue

            if isinstance(value, (list, set, tuple)):
                params.extend([(key, v) for v in value])
            else:
                params.append((key, value))

        return params, sliced_d

    def _valid_params(self, **kwargs) -> LDAny:
        """Return list of kwargs-params, ready for multiple requests.

        - raise ERROR if any of kwargs-params is not allowed.
        - raise ERROR if multiple iterable-params in kwargs.
        """
        conc_keys = set(kwargs).intersection(set(self._concurrent))
        conc_keys = {k for k, v in kwargs.items() if k in conc_keys and self._is_iterable(v)}
        if not conc_keys:
            return [kwargs]

        kwargs_: LDAny = []
        kwargs_wo_conc = {k: v for k, v in kwargs.items() if k not in conc_keys}
        for key in sorted(conc_keys):
            values = kwargs[key]
            for value in values:
                kwargs_.append({**kwargs_wo_conc, **{key: value}})

        # remove duplicate values
        for kwargs_d in kwargs_:
            for key, value in kwargs_d.items():
                kwargs_d[key] = _validate_value(value)

        return kwargs_

    def _generate_slices(self, key: str, values: LValue, params: LParam, /) -> LTInt2:
        """Generate start and end indexes of parameters, ready for URL slicing.

        :param key: The key of the parameter that needs to be sliced.
        :param values: The values of the parameter that need to be sliced.
        :param params: Other parameters that need to be mentioned in the URL.
        :return: The start and end indexes of the parameters, ready for URL slicing.
        """
        if len(values) <= 1:
            return [(0, 1)]

        slices: LTInt2 = []
        start = 0
        for end in range(1, len(values) + 1):
            end_ = end + 1
            params_ = params + [("offset", self.limit), ("limit", self.limit)]
            params_ += [(key, s) for s in values[start:end_]]
            url = f"{self.url}/api/{self._query}?{urlencode(params_)}"
            if end_ < len(values) + 1 and len(url) < self.url_max_len:
                continue
            slices.append((start, end))
            start = end
        return slices

    @staticmethod
    def _check_keys(items: LDAny, required: SeStr = None, denied: SeStr = None) -> bool:
        """Return True if all required-keys present and denied-keys absent in data."""
        absent_keys: SStr = set()
        denied_keys: SStr = set()
        for data in items:
            for key in required or []:
                if key not in data:
                    absent_keys.add(key)
                    msg = f"absent {key=} in Netbox {data=}"
                    logging.error(msg)
            for key in denied or []:
                if key in data:
                    denied_keys.add(key)
                    msg = f"found denied {key=} in Netbox {data=}"
                    logging.error(msg)
        if absent_keys or denied_keys:
            invalid_keys = [*absent_keys, *denied_keys]
            raise NbApiError(f"Netbox data {invalid_keys=}")
        return True

    @staticmethod
    def _no_vrf(items: LDAny) -> LDAny:
        """Return data without vrf."""
        return [d for d in items if not d.get("vrf")]

    def _slice_params(self, params_d: DAny) -> LDAny:
        """Generate sliced parameters, ready for URLs with valid length.

        If the length of the URL exceeds maximum allowed (due to a large number of parameters),
        then need split (slice) the request into multiple parts.
        :param params_d: Finding parameters, where one of key/value need be sliced.
        :return: Sliced parameters.
        :example:
            _slice_params(params_d={"address": ["10.0.0.0", "10.0.0.1"], "family": 4}) ->
            [{"address": ["10.0.0.0"], "family": 4}, {"address": ["10.0.0.1"], "family": 4}]
        """
        values: LValue = _validate_values(values=params_d[self._sliced])
        params: LParam = [(k, v) for k, v in params_d.items() if k != self._sliced]
        slices: LTInt2 = self._generate_slices(self._sliced, values, params)

        params_sliced: LDAny = []
        for start, end in slices:
            params_l: LParam = params + [(self._sliced, s) for s in values[start:end]]
            params_sliced_: DAny = h.params_to_dict(params_l)
            params_sliced.append(params_sliced_)
        return params_sliced

    def _slice_params_counters(self, results: LDAny) -> LDAny:
        """Generate sliced parameters based on counts in results.

        To request data in threading mode need have all params with offsets.
        :param results: List of dicts with params_d and related counts of objects.
        :return: Sliced parameters.
        """
        params: LDAny = []
        for result in results:
            count = result["count"]
            params_d = result["params_d"]
            if not result["count"]:
                continue
            if count <= self.limit:
                params.append(params_d)
                continue
            params_: LDAny = _generate_offsets(count, self.limit, params_d)
            params.extend(params_)
        return params

    # ============================== is ==============================

    @staticmethod
    def _is_iterable(arg: Any) -> bool:
        """Return True if arg is iterable."""
        if isinstance(arg, Iterable) and not isinstance(arg, str):
            return True
        return False

    @staticmethod
    def _is_status_code_400(response: Response) -> bool:
        """Return True if status_code 4xx."""
        if 400 <= response.status_code < 500:
            return True
        return False

    @staticmethod
    def _is_status_code_500(response: Response) -> bool:
        """Return True if status_code 5xx."""
        if 500 <= response.status_code < 600:
            return True
        return False

    @staticmethod
    def _is_credentials_error(response: Response) -> bool:
        """Return True if invalid credentials."""
        if response.status_code == 403:
            if re.search("Invalid token", response.text, re.I):
                return True
        return False

    @staticmethod
    def _is_not_available_error(response: Response) -> bool:
        """Return True if the object (tag) absent in Netbox."""
        if response.status_code == 400:
            return True
        return False

    # =========================== messages ===========================

    @staticmethod
    def _msg_status_code(response: Response) -> str:
        """Return message ready for logging ConnectionError."""
        if not hasattr(response, "status_code"):
            return ""
        status_code, text, url = response.status_code, response.text, response.url
        return f"{status_code=} {text=} {url=}"

    # ======================== params helpers ========================

    def _param_vrf(self, **kwargs) -> DAny:
        """Change "vrf" name to "vrf_id" in kwargs."""
        vrf = kwargs.get("vrf") or ""
        if not vrf:
            return kwargs
        vrfs = h.list_(vrf)
        vrfs_d: LDAny = self.query(query="ipam/vrfs/")
        vrfs_d = [d for d in vrfs_d if d["name"] in vrfs]
        if not vrfs_d:
            return kwargs

        vrf_ids = [d["id"] for d in vrfs_d]
        del kwargs["vrf"]
        kwargs["vrf_id"] = vrf_ids
        return kwargs


# ============================= init =============================

def _init_threads(**kwargs) -> int:
    """Init threads count, default 1."""
    threads = int(kwargs.get("threads") or 1)
    if threads < 1:
        threads = 1
    return int(threads)


# ============================= helpers ==========================

def _generate_offsets(count: int, limit: int, params_d: DAny, /) -> LDAny:
    """Generate a list of dictionaries with offset parameters.

    :param count: The total count of items to be processed.
    :param limit: The maximum limit for each batch.
    :param params_d: A dictionary containing other parameters.
    :return: A list of dictionaries with offset and other parameters.
    """
    if count <= 0 or limit <= 0:
        raise ValueError(f"{count=} {limit=}, value higher that 1 expected.")

    params: LDAny = []
    offset = 0
    while count > 0:
        limit_ = min(count, limit)
        params_d_ = params_d.copy()
        params_d_["limit"] = limit
        params_d_["offset"] = offset
        params.append(params_d_)
        offset += limit_
        count -= limit_

    return params


def _validate_value(value: Any) -> LValue:
    """Check typing, remove duplicate values from list.

    :param value: The value to be validated.
    :return: A valid value.
    """
    if isinstance(value, TValues):
        return value
    if not isinstance(value, TLists):
        raise TypeError(f"{value=}, {TValues} expected")

    values: LValue = []
    for value_ in value:
        if not isinstance(value_, TValues):
            raise TypeError(f"{value_=}, {TValues} expected")
        values.append(value_)

    values = h.no_dupl(values)
    return values


def _validate_values(values: Any) -> LValue:
    """Convert a value to a list and remove duplicates.

    :param values: The value to be converted.
    :return: A list of values.
    """
    if isinstance(values, TValues):
        return [values]
    values_ = _validate_value(values)
    return values_
