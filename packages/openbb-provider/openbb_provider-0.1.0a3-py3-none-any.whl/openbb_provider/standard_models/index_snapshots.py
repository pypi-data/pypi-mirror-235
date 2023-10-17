"""Index Snapshots  data model."""

from typing import Literal, Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams


class IndexSnapshotsQueryParams(QueryParams):
    """Index Search Query Params"""

    region: Optional[Literal["US", "EU"]] = Field(
        description="The region to return. Currently supports US and EU.", default="US"
    )


class IndexSnapshotsData(Data):
    """Index Snapshot Data."""

    symbol: str = Field(description="Symbol of the index.")
    name: Optional[str] = Field(default=None, description="Name of the index.")
    currency: Optional[str] = Field(default=None, description="Currency of the index.")
    price: Optional[float] = Field(
        default=None, description="Current price of the index."
    )
    open: Optional[float] = Field(
        default=None, description="Opening price of the index."
    )
    high: Optional[float] = Field(
        default=None, description="Highest price of the index."
    )
    low: Optional[float] = Field(default=None, description="Lowest price of the index.")
    close: Optional[float] = Field(
        default=None, description="Closing price of the index."
    )
    prev_close: Optional[float] = Field(
        default=None, description="Previous closing price of the index."
    )
    change: Optional[float] = Field(default=None, description="Change of the index.")
    change_percent: Optional[float] = Field(
        default=None, description="Change percent of the index."
    )
