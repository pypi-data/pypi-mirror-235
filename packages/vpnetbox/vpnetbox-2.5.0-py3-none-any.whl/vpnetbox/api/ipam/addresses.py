"""Addresses."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Addresses(Base):
    """Addresses."""

    def __init__(self, **kwargs):
        """Init Addresses.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "ipam/ip-addresses/"
        self._sliced = "address"
        self._concurrent = (
            "assigned_to_interface",
            "family",
            "mask_length",
            "parent",
            "q",
            "status",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get ip-addresses objects from Netbox.

        :param kwargs: Finding parameters.

        ===================== =================== ==================================================
        Parameter             single-value        multiple-values
        ===================== =================== ==================================================
        address               "10.0.0.1/26"       ["10.0.0.1/26", "10.0.0.2/26"]
        id                    25564               [25564, 42646]
        q                     "10.0.0."           ["10.0.0.", "10.31.65."]
        tag                   "tag1"              [tag1", "tag2"]
        parent                "10.0.0.0/26"       ["10.0.0.0/26", "10.31.65.0/26"]
        family                4                   [4, 6]
        status                "active"            ["reserved", "deprecated"]
        role                  "vip"               ["vip", "loopback"]
        mask_length           24                  [24, 32]
        assigned_to_interface True, False
        vrf                   "vrf1"              ["vrf1", "vrf2"]
        vrf_id                40                  [40, 41]
        tenant                "tenant1"           ["tenant1", "tenant2"]
        ===================== =================== ==================================================

        :return: List of ip-addresses objects.
        """
        kwargs = self._param_vrf(**kwargs)
        params: LDAny = self._valid_params(**kwargs)
        params = self._add_default_to_params(*params)

        items: LDAny = self._query_params_ld(params)

        if not (kwargs.get("vrf_id") or self.default.get("vrf_id")):
            items = self._no_vrf(items=items)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
