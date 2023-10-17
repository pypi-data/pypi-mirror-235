# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

from __future__ import annotations

import sys
from collections import namedtuple
from enum import Enum
from typing import (
    Any,
    Callable,
    Optional,
    Type,
    TypeVar,
    Union,
)

import numpy as np
from qctrlcommons.exceptions import QctrlArgumentsValueError
from qctrlcommons.preconditions import check_argument

if sys.version_info >= (3, 10):
    from typing import (
        Concatenate,
        ParamSpec,
    )
else:
    from typing_extensions import (
        Concatenate,
        ParamSpec,
    )


T = TypeVar("T", bound=Enum)


def validate_enum(enum_: Type[T], item: T | str) -> str:
    """
    Check whether the item is a valid option in enum_. If so, return the name of that option.
    Otherwise, raise an error.

    Parameters
    ----------
    enum_ : T
        An Enum where we expect the option value to be a str.
    item : T or str
        The item to be checked with enum_.

    Returns
    -------
    str
        The name of a valid enum option.
    """
    if isinstance(item, enum_):
        return item.name
    try:
        return getattr(enum_, item).name  # type: ignore
    except (TypeError, AttributeError) as err:
        raise QctrlArgumentsValueError(
            "Only the following options are allowed: " f"{list(enum_.__members__)} ",
            arguments={"item": item},
        ) from err


def _is_integer(val: Any) -> bool:
    return isinstance(val, ScalarDType.INT.value.types)


def _is_real(val: Any) -> bool:
    return _is_integer(val) or isinstance(val, ScalarDType.REAL.value.types)


def _is_complex(val: Any) -> bool:
    return _is_real(val) or isinstance(val, ScalarDType.COMPLEX.value.types)


def _is_number(val: Any) -> bool:
    return _is_real(val) or _is_complex(val)


def _number_converter(val: Any) -> int | float | complex:
    if _is_integer(val):
        return int(val)
    if _is_real(val):
        return float(val)
    return complex(val)


# types: supported types defined by Python and Numpy for a given dtype
# checker: a callable to check the input scalar
# converter: a callable to convert the scalar to the corresponding Python primitive type
_ScalarDTypeValidator = namedtuple(
    "_ScalarDTypeValidator", ["types", "checker", "converter"]
)

_SCALAR = TypeVar(
    "_SCALAR", bound=Union[int, float, complex, np.integer, np.float_, np.complex_]
)


class ScalarDType(Enum):
    """
    Store dtypes to validate both Python and NumPy types.
    """

    INT = _ScalarDTypeValidator((int, np.integer), _is_integer, int)
    REAL = _ScalarDTypeValidator((float, np.float_), _is_real, float)
    COMPLEX = _ScalarDTypeValidator((complex, np.complex_), _is_complex, complex)
    NUMBER = _ScalarDTypeValidator(None, _is_number, _number_converter)

    def __call__(
        self,
        value: _SCALAR,
        name: str,
        min_: Optional[Any] = None,
        max_: Optional[Any] = None,
        min_inclusive: bool = False,
        max_inclusive: bool = False,
    ) -> _SCALAR:
        """
        Validate a given scalar by the dtype.
        If valid, return the value as a primitive Python numeric type.
        """
        check_argument(
            self.value.checker(value),
            f"The {name} must be a {self.name.lower()}.",
            {name: value},
        )

        if min_ is not None:
            check_argument(
                value > min_ or (min_inclusive and value == min_),
                f"The {name} must be greater than {'or equal to' if min_inclusive  else ''} "
                f"{min_}.",
                {name: value},
            )
        if max_ is not None:
            check_argument(
                value < max_ or (max_inclusive and value == max_),
                f"The {name} must be smaller than {'or equal to' if max_inclusive  else ''} "
                f"{max_}.",
                {name: value},
            )
        return self.value.converter(value)


# valid_dtype_kinds: valid values for the array's dtype.kind.
# dtype: data type of the returned validated NumPy array
_ArrayDTypeValidator = namedtuple(
    "_ArrayDTypeValidator", ["valid_dtype_kinds", "dtype"]
)


class ArrayDType(Enum):
    """
    Store dtypes to validate array-likes.
    """

    INT = _ArrayDTypeValidator("iu", np.integer)
    REAL = _ArrayDTypeValidator("iuf", np.float_)
    COMPLEX = _ArrayDTypeValidator("iufc", np.complex_)
    NUMERIC = _ArrayDTypeValidator("iufc", None)

    def __call__(
        self,
        value: Any,
        name: str,
        ndim: Optional[int] = None,
        shape: Optional[tuple] = None,
        min_: Optional[Any] = None,
        max_: Optional[Any] = None,
        min_inclusive: bool = False,
        max_inclusive: bool = False,
    ) -> np.ndarray:
        """
        Validate a given array-like by the dtype.
        If valid, return the value as a NumPy array with the corresponding dtype.
        """
        array_val = np.asarray(value)

        check_argument(
            array_val.size > 0, f"The {name} must not be an empty array.", {name: value}
        )

        check_argument(
            array_val.dtype.kind in self.value.valid_dtype_kinds,
            f"The {name} must be a {self.name.lower()} array.",
            {name: value},
        )

        if ndim is not None:
            check_argument(
                array_val.ndim == ndim,
                f"The {name} must be a {ndim}D array.",
                {name: value},
            )
        if shape is not None:
            check_argument(
                array_val.shape == shape,
                f"The {name} must be an array with shape {shape}.",
                {name: value},
            )

        if min_ is not None:
            check_argument(
                np.all(array_val > min_)
                or (min_inclusive and np.all(array_val >= min_)),
                f"The values in the {name} must be greater than "
                f"{'or equal to' if min_inclusive  else ''} {min_}.",
                {name: value},
            )
        if max_ is not None:
            check_argument(
                np.all(array_val < max_)
                or (max_inclusive and np.all(array_val <= max_)),
                f"The values in the {name} must be smaller than "
                f"{'or equal to' if max_inclusive  else ''} {max_}.",
                {name: value},
            )
        # Special handler for cases:
        # - int typed array to address the signed and unsigned cases.
        # - a generic numeric array
        # That is, we preserve the dtype from users in these cases.
        if self in (ArrayDType.INT, ArrayDType.NUMERIC):
            return array_val
        try:
            return array_val.astype(self.value.dtype, casting="safe")
        except TypeError as err:
            raise QctrlArgumentsValueError(
                f"Expected {name} as an array of {self.name.lower()} dtype, "
                f"but got {array_val.dtype}.",
                {name: value},
            ) from err


_VAL = TypeVar("_VAL")
P = ParamSpec("P")


def nullable(
    validator: Callable[Concatenate[_VAL, P], _VAL],
    value: Optional[_VAL],
    *args: P.args,
    **kwargs: P.kwargs,
) -> Optional[_VAL]:
    """
    Validate a parameter that can be None.

    When the parameter holds a non-null value, the validator callable is used to check the value.
    The validator takes the value as the first argument and some other options as defined by P, it
    returns the same type as the input value (strictly speaking, the returned type is something
    that can be converted from the input one. But in reality, we expect  we expect them to be
    interchangeable). The P annotation here allows mypy to also check the types for the
    resting arguments of the validator.
    """
    if value is None:
        return value
    return validator(value, *args, **kwargs)
