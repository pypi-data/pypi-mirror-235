"""Typing."""
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union, Sequence, TypeVar

# one-level
DAny = Dict[str, Any]
DInt = Dict[str, int]
DObj = Dict[str, object]
DStr = Dict[str, str]
LBool = List[bool]
LInt = List[int]
LPath = List[Path]
LStr = List[str]
LTInt2 = List[Tuple[int, int]]
ODatetime = Optional[datetime]
Param = Tuple[str, Any]
SInt = Set[int]
SStr = Set[str]
SeStr = Sequence[str]
StrInt = Union[str, int]
T2Str = Tuple[str, str]
T3Str = Tuple[str, str, str]
TLists = (list, set, tuple)
TStr = Tuple[str, ...]
TValues = (str, int, float)
Type = TypeVar("Type")
Value = Union[str, int, float]

# two-level
DDAny = Dict[str, DAny]
DDStr = Dict[str, DStr]
DLStr = Dict[str, LStr]
DSStr = Dict[str, SStr]
DiDAny = Dict[int, DAny]
DiStr = Dict[int, str]
LDAny = List[DAny]
LDStr = List[DStr]
LParam = List[Param]
LTup2 = List[T2Str]
LType = List[Type]
LValue = List[Value]
SParam = Set[Param]
SeDAny = Sequence[DAny]
SeType = Sequence[Type]
T3SStr = Tuple[SStr, SStr, SStr]
TParam = Tuple[Param, ...]
UStr = Union[str, SeStr]

# three-level
UParam = Union[LParam, SParam, TParam]
DDDLStr = Dict[str, Dict[str, DLStr]]
LLDAny = List[LDAny]
LLParam = List[LParam]
OUStr = Optional[UStr]
