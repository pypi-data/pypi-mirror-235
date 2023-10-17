"""Helper functions."""

import re
from typing import Any, Iterable

from vpnetbox.types_ import DAny, T2Str, T3Str, SeType, LType, LParam, TLists, UParam


# =============================== str ================================

def findall1(pattern: str, string: str, flags=0) -> str:
    """Parse 1st item of re.findall(). If nothing is found, returns an empty string.

    Group with parentheses in pattern is required.
    :return: Interested substring.
    :example:
        findall1(pattern="a(b)cde", string="abcde") -> "b"
    """
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [""])[0]
    if isinstance(result, str):
        return result
    if isinstance(result, tuple):
        return result[0]
    return ""


def findall2(pattern: str, string: str, flags=0) -> T2Str:
    """Parse 2 items of re.findall(). If nothing is found, returns 2 empty strings.

    Group with parentheses in pattern is required.
    :return: Two interested substrings.
    :example:
        findall2(pattern="a(b)(c)de", string="abcde") -> "b", "c"
    """
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [("", "")])[0]
    if isinstance(result, tuple) and len(result) >= 2:
        return result[0], result[1]
    return "", ""


def findall3(pattern: str, string: str, flags=0) -> T3Str:
    """Parse 3 items of re.findall(). If nothing is found, returns 3 empty strings.

    Group with parentheses in pattern is required.
    :return: Three interested substrings.
    :example:
        findall3(pattern="a(b)(c)(d)e", string="abcde") -> "b", "c", "d"
    """
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [("", "", "")])[0]
    if isinstance(result, tuple) and len(result) >= 3:
        return result[0], result[1], result[2]
    return "", "", ""


# =============================== list ===============================

def list_(items) -> list:
    """Return list of not-empty-items with the same type_."""
    if not items:
        return []
    if isinstance(items, str) or not isinstance(items, Iterable):
        return [items]
    return list(items)


def no_dupl(items: SeType) -> LType:
    """Remove duplicate items from list."""
    items_ = []
    for item in items:
        if item not in items_:
            items_.append(item)
    return items_


# =============================== dict ===============================

def pop_d(key: str, data: DAny) -> Any:
    """Remove the specified item from the data by key."""
    if key in data:
        value = data.pop(key)
        return value
    return None


def dict_to_params(params_d: DAny) -> LParam:
    """Convert a dictionary to a list of tuples.
    
    :param params_d: A dictionary with keys and values.
    :return:  A list of tuples.
    """
    params: LParam = []
    for key, value in params_d.items():
        if isinstance(value, TLists):
            for value_ in value:
                params.append((key, value_))
        else:
            params.append((key, value))
    return params


def params_to_dict(params: UParam) -> DAny:
    """Convert a list of tuples to a dictionary.

    :param params: A list of tuples.
    :return: A dictionary with keys and values.
    """
    params_d: DAny = {}
    for key, value in params:
        if key in params_d:
            if isinstance(params_d[key], list):
                params_d[key].append(value)
            else:
                params_d[key] = [params_d[key], value]
        else:
            params_d[key] = value
    return params_d
