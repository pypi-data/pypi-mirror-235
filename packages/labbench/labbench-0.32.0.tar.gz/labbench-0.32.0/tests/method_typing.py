from __future__ import annotations
import typing
from typing import Callable, TypeVar, Dict, Tuple, Type, List, Sequence, cast, get_type_hints, Concatenate, Any, Protocol
from typing_extensions import TypeVarTuple, Unpack, ParamSpec
import functools
import labbench as lb
from dataclasses import dataclass, make_dataclass

Ts = TypeVarTuple('Ts')
P = ParamSpec('P')

def whatever(*args, **kws):
    """docs"""
    pass

def method_factory(*args: Unpack[Ts]) -> Callable[[Unpack[Ts]]]:
    @functools.wraps(whatever)
    def myfunc(*a):
        return 7

    return myfunc

func = method_factory(lb.value.str.__init__, lb.value.bytes)


print(func.__annotations__)