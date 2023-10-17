"""NbHandler, Retrieves and caches a bulk of data from the Netbox to local system.

Collects sets of aggregates, prefixes, addresses, devices, sites data from Netbox by scenarios.
"""

from __future__ import annotations

import logging
from typing import Iterable

from vpnetbox.api.nb_api import NbApi
from vpnetbox.api.nb_parser import NbParser
from vpnetbox.cache import Cache, make_path
from vpnetbox.messages import Messages
from vpnetbox.nbh.nb_data import NbData
from vpnetbox.types_ import LStr, SStr, DAny


class NbHandler(Cache):
    """NbHandler, Retrieves and caches a bulk of data from the Netbox to local system.

    Collects sets of aggregates, prefixes, addresses, devices, sites data from Netbox by scenarios.
    """

    def __init__(self, **kwargs):
        """Init NbHandler.

        :param kwargs: Parameters.

        Params for NbApi.

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

        Params for NbData.
        :param aggregates LDict: List of Netbox aggregates data.
        :param prefixes LDict: List of Netbox prefixes data.
        :param addresses LDict: List of Netbox addresses data.
        :param devices LDict: List of Netbox devices data.
        :param sites LDict: List of Netbox sites data.

        Params for Cache.
        :param var str: Path to var directory for cache file.
        """
        cache_params = self._init_cache_params(**kwargs)
        Cache.__init__(self, **cache_params)
        self.api = NbApi(**kwargs)
        self.msgs = Messages(name=self.api.host)

        self.data = NbData(**kwargs)

    def __repr__(self) -> str:
        """__repr__."""
        return self.data.__repr__().replace(self.data.name, self.name)

    # ============================= init =============================

    def _init_cache_params(self, **kwargs) -> DAny:
        """Init params for Cache."""
        path: str = make_path(**kwargs, **{"name": self.__class__.__name__})
        return dict(cache_path=path, cache_attrs=["data"])

    # ========================== scenarios ===========================

    def get_addresses(self, **kwargs) -> None:
        """Get Netbox ipam/addresses objects with specified parameters in kwargs."""
        self.data.addresses = self.api.addresses.get(**kwargs)

    def get_aggregates(self, **kwargs) -> None:
        """Get Netbox ipam/aggregates objects with specified parameters in kwargs."""
        self.data.aggregates = self.api.aggregates.get(**kwargs)

    def get_circuits(self, **kwargs) -> None:
        """Get Netbox circuits/circuits objects with specified parameters in kwargs."""
        self.data.circuits = self.api.circuits.get(**kwargs)

    def get_devices(self, **kwargs) -> None:
        """Get Netbox dcim/devices objects with specified parameters in kwargs."""
        self.data.devices = self.api.devices.get(**kwargs)

    def get_prefixes(self, **kwargs) -> None:
        """Get Netbox ipam/prefixes objects with specified parameters in kwargs."""
        self.data.prefixes = self.api.prefixes.get(**kwargs)

    def get_vlans(self, **kwargs) -> None:
        """Get Netbox ipam/vlans objects with specified parameters in kwargs."""
        self.data.vlans = self.api.vlans.get(**kwargs)

    def get_sites(self, **kwargs) -> None:
        """Get Netbox dcim/sites objects with specified parameters in kwargs."""
        self.data.sites = self.api.sites.get(**kwargs)

    def get_terminations(self, **kwargs) -> None:
        """Get Netbox circuits/terminations objects with specified parameters in kwargs."""
        self.data.terminations = self.api.terminations.get(**kwargs)

    def scenario__demo(self) -> None:
        """Get minimum of aggregates/prefixes/addresses/devices for this tool demonstration.

        Save received data to self object.
        :return: None. Update self object.
        """
        aggregates = ["10.10.0.0/16", "10.31.64.0/18"]
        prefixes = ["10.10.0.0/24", "10.10.119.0/26", "10.31.65.0/26", "10.31.67.0/26"]
        addresses = ["10.10.0.1/24", "10.10.119.1/26", "10.31.65.18/26", "10.31.67.17/26"]
        devices = ["device1", "device2"]
        self.api.default_active()
        self.data.version = self.api.version()
        self.get_aggregates(prefix=aggregates)
        self.get_prefixes(prefix=prefixes)
        self.get_addresses(address=addresses)
        self.get_devices(name=devices)
        logging.debug("%s data loaded.", f"{self!r}")

    # =========================== method =============================

    def clear(self) -> None:
        """Delete all data in NbData."""
        self.data.clear()

    def devices_primary_ip4(self) -> LStr:
        """Return primary_ip4 of Netbox devices.

        :return: addresses.
        """
        parsers = [NbParser(data=d) for d in self.data.devices]
        primary_ip4: SStr = {o.device_primary_ip4() for o in parsers}
        return sorted(primary_ip4)

    def set_addresses_mask_32(self) -> None:
        """Change mask to /32 for all Netbox addresses."""
        for data in self.data.addresses:
            address = data["address"]
            data["address"] = address.split("/")[0] + "/32"

    # ===================== public data helpers ======================

    def copy(self) -> NbHandler:
        """Return copy of self NbData (deepcopy)."""
        kwargs = dict(host=self.api.host,
                      token=self.api.addresses.token,
                      verify=self.api.addresses.verify,
                      limit=self.api.addresses.limit,
                      timeout=self.api.addresses.timeout,
                      max_retries=self.api.addresses.max_retries,
                      sleep=self.api.addresses.sleep,
                      url_max_len=self.api.addresses.url_max_len)
        nb_handler = NbHandler(**kwargs)
        nb_handler.data = self.data.copy()
        return nb_handler

    def is_empty(self) -> bool:
        """Return True if NbData is empty (has no any data)."""
        return self.data.is_empty()

    def print_warnings(self) -> None:
        """Print WARNINGS if found some errors/warnings in data processing."""
        for datas in [self.data.aggregates, self.data.prefixes, self.data.addresses]:
            for data in datas:
                if warnings := data.get("warnings") or []:
                    for msg in warnings:
                        logging.warning(msg)

    # =========================== helper =============================

    @staticmethod
    def _no_duplicates(items: Iterable) -> list:
        """Return list of items without duplicates."""
        items_ = []
        for item in items:
            if item not in items_:
                items_.append(item)
        return items_
