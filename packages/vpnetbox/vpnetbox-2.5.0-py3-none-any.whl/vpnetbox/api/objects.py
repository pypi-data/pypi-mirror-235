"""Objects."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Objects(Base):
    """Objects."""

    def __init__(self, **kwargs):
        """Init Objects.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = str(kwargs.get("query") or "")
        self._concurrent = ("q", "status", "tag")

    def get(self, **kwargs) -> LDAny:
        """Get objects from Netbox.

        :param kwargs: Finding parameters.

        =============== ============================== =============================================
        Parameter       single-value                   multiple-values
        =============== ============================== =============================================
        id              25564                          [25564, 42646]
        q               "10.0.0."                      ["10.0.0.", "10.31.65."]
        status          "active"                       ["reserved", "deprecated"]
        =============== ============================== =============================================

        :return: *List[dict]* List of objects.
        """
        params: LDAny = self._valid_params(**kwargs)
        params = self._add_default_to_params(*params)
        items: LDAny = self._query_params_ld(params)
        return items
