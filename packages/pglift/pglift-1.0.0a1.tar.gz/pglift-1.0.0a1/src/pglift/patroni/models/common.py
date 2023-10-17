import functools
from typing import Any

from pydantic import Field, validator

from ... import types


class RESTAPI(types.BaseModel):
    connect_address: types.Address = Field(
        default_factory=functools.partial(types.Address.get, port=8008),
        description="IP address (or hostname) and port, to access the Patroni's REST API.",
    )
    listen: types.Address = Field(
        default_factory=types.Address.unspecified,
        description="IP address (or hostname) and port that Patroni will listen to for the REST API. Defaults to connect_address if not provided.",
    )

    @validator("listen", always=True, pre=True)
    def __validate_listen_(cls, value: str, values: dict[str, Any]) -> str:
        """Set 'listen' from 'connect_address' if unspecified.

        >>> RESTAPI()  # doctest: +ELLIPSIS
        RESTAPI(connect_address='...:8008', listen='...:8008')
        >>> RESTAPI(connect_address="localhost:8008")
        RESTAPI(connect_address='localhost:8008', listen='localhost:8008')
        >>> RESTAPI(connect_address="localhost:8008", listen="server:123")
        RESTAPI(connect_address='localhost:8008', listen='server:123')
        """
        if not value:
            value = values["connect_address"]
            assert isinstance(value, str)
        return value
