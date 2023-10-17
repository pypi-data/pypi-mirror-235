from typing import (Optional, Union, List, Iterator, Protocol, Dict, Any, Tuple)
from datetime import datetime as datetime_

class GeoInterface(Protocol):
    @property
    def __geo_interface__(self) -> Dict[str, Any]:
        ...

Collections = Tuple[str, ...]
CollectionsLike = Union[List[str], Iterator[str], str]

Intersects = Dict[str, Any]
IntersectsLike = Union[str, GeoInterface, Intersects]

DatetimeOrTimestamp = Optional[Union[datetime_, str]]
Datetime = str
DatetimeLike = Union[
    DatetimeOrTimestamp,
    Tuple[DatetimeOrTimestamp, DatetimeOrTimestamp],
    List[DatetimeOrTimestamp],
    Iterator[DatetimeOrTimestamp],
]

FilterLike = Union[Dict[str, Any], str]

Sortby = List[Dict[str, str]]
SortbyLike = Union[Sortby, str, List[str]]


class ItemSearch:
    pass