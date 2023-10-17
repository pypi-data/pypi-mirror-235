"""NbApi, Python wrapper of Netbox REST API.

Requests data from the Netbox REST API using filter parameters identical
to those in the web interface filter form.
"""

from __future__ import annotations

from vpnetbox import helpers as h
from vpnetbox.api.circuits.circuits import Circuits
from vpnetbox.api.circuits.terminations import Terminations
from vpnetbox.api.dcim.device_types import DeviceTypes
from vpnetbox.api.dcim.devices import Devices
from vpnetbox.api.dcim.sites import Sites
from vpnetbox.api.ipam.addresses import Addresses
from vpnetbox.api.ipam.aggregates import Aggregates
from vpnetbox.api.ipam.asns import Asns
from vpnetbox.api.ipam.ip_ranges import IpRanges
from vpnetbox.api.ipam.prefixes import Prefixes
from vpnetbox.api.ipam.rirs import Rirs
from vpnetbox.api.ipam.roles import Roles
from vpnetbox.api.ipam.vlans import Vlans
from vpnetbox.api.ipam.vrfs import Vrfs
from vpnetbox.api.objects import Objects


class NbApi:
    """NbApi, Python wrapper of Netbox REST API.

    Requests data from the Netbox REST API using filter parameters identical
    to those in the web interface filter form.
    """

    def __init__(self, **kwargs):
        """Init NbApi.

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
        self.host = _init_host(**kwargs)
        self.token = str(kwargs.get("token") or "")
        # ipam
        self.addresses = Addresses(**kwargs)
        self.aggregates = Aggregates(**kwargs)
        self.asns = Asns(**kwargs)
        self.ip_ranges = IpRanges(**kwargs)
        self.prefixes = Prefixes(**kwargs)
        self.rirs = Rirs(**kwargs)
        self.roles = Roles(**kwargs)
        self.vlans = Vlans(**kwargs)
        self.vrfs = Vrfs(**kwargs)
        # dcim
        self.device_types = DeviceTypes(**kwargs)
        self.devices = Devices(**kwargs)
        self.sites = Sites(**kwargs)
        # circuits
        self.circuits = Circuits(**kwargs)
        self.terminations = Terminations(**kwargs)
        # universal
        self.objects = Objects(**kwargs)
        self.get = self.objects.query
        self.version = self.objects.version

    def __repr__(self) -> str:
        """__repr__."""
        name = self.__class__.__name__
        return f"<{name}: {self.host}>"

    # =========================== method =============================
    def default_active(self):
        """Set default params, ready for working with active devices/prefixes."""
        self.aggregates.default = dict(family=4)
        self.prefixes.default = dict(family=4, status=["active", "container"])
        self.addresses.default = dict(family=4, status="active")
        self.vlans.default = dict(status="active")
        self.devices.default = dict(has_primary_ip=True, status="active")


# ============================= init =============================

def _init_host(**kwargs) -> str:
    """Init Netbox host name."""
    host = str(kwargs.get("host") or "")
    host = h.findall1(r"^(?:\w+://)?(.+)", host)
    return host
