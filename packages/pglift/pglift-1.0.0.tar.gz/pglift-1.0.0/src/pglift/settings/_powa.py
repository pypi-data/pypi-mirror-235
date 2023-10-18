from pydantic import Field

from .base import BaseModel


class Settings(BaseModel):
    """Settings for PoWA."""

    dbname: str = Field(default="powa", description="Name of the PoWA database")
    role: str = Field(default="powa", description="Instance role used for PoWA.")
