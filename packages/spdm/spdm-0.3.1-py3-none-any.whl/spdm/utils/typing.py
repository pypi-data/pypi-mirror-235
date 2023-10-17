import collections.abc
import dataclasses
import inspect
import typing
from dataclasses import dataclass
from enum import Enum
import types
import numpy as np
import numpy.typing as np_tp

from .logger import logger, deprecated
from .tags import _not_found_

ArrayLike = np_tp.ArrayLike | None

boolean_type = (bool,)

integral_type = (int, np.integer,)

real_type = (float, np.floating,)

bitwise_and_reduce = np.bitwise_and.reduce

complex_type = (complex, np.complexfloating,)

ScalarType = bool | int | float | complex | np.float64 | np.complex64 | np.complex128 | np.integer | np.floating | np.bool_ | None

scalar_type = (*boolean_type, *integral_type, *real_type, *complex_type)

ArrayType = np_tp.NDArray[np.floating | np.complexfloating]

array_type = np.ndarray

NumericType = ScalarType | ArrayType

numeric_type = (*scalar_type, array_type)

PrimaryType = str | NumericType | Enum

primary_type = (str,  *numeric_type)

NativeType = PrimaryType | dict | list

native_type = (dict, list, *primary_type)

_T = typing.TypeVar("_T")

HTContainer = _T | typing.Sequence[_T]
"""Hierarchical Container Type  """

HNodeLike = None | int | str | bool | ArrayType

HTreeLike = dict | list | HNodeLike


@dataclass
class Vector2:
    x: float
    y: float


@dataclass
class Vector3:
    x: float
    y: float
    z: float


@dataclass
class Vector4:
    x: float
    y: float
    z: float
    t: float


nTupleType = typing.Tuple[ScalarType, ...]


def is_vector(v: typing.Any) -> bool:
    return isinstance(v, collections.abc.Sequence) and all(is_scalar(d) for d in v)


def is_array(v: typing.Any) -> bool:
    return (isinstance(v, array_type) and len(v.shape) > 0)


def is_numeric(v: typing.Any) -> bool:
    return isinstance(v, numeric_type)


def is_complex(d: typing.Any) -> bool:
    return np.iscomplexobj(d)


def is_real(d: typing.Any) -> bool:
    return not np.iscomplexobj(d)


# def is_scalar(d: typing.Any) -> bool:
#     return isinstance(d, (int, float, complex, np.floating, np.complexfloating)) or hasattr(d.__class__, "__float__")
is_scalar = np.isscalar


def as_scalar(d: typing.Any) -> ScalarType:
    return complex(d) if is_complex(d) else float(d)


def as_array(d: typing.Any, *args, **kwargs) -> ArrayType:
    if d is None or d is _not_found_:
        return d
    elif isinstance(d, array_type):
        return d
    elif hasattr(d, '__array__'):
        return d.__array__()
    elif hasattr(d.__class__, '__value__'):
        return np.asarray(d.__value__, *args,  **kwargs)
    else:
        return np.asarray(d, *args,  **kwargs)


def normalize_array(value: ArrayLike, *args, **kwargs) -> ArrayType:
    """ 将 value 转换为 array_type 类型 """
    if isinstance(value, array_type) or is_scalar(value):
        pass
    elif value is None or value is _not_found_:
        value = None
    elif isinstance(value, numeric_type):
        value = as_array(value, *args, **kwargs)
    elif isinstance(value, tuple):
        value = as_array(value, *args, **kwargs)
    elif isinstance(value, collections.abc.Sequence):
        value = as_array(value, *args, **kwargs)
    elif isinstance(value, collections.abc.Mapping) and len(value) == 0:
        value = None
    else:
        raise RuntimeError(f"Function._normalize_value() incorrect value {value}! {type(value)}")

    if isinstance(value, array_type) and value.size == 1:
        value = np.squeeze(value).item()

    return value


def as_dataclass(cls, value):
    if not dataclasses.is_dataclass(cls):
        raise TypeError(type(cls))
    elif isinstance(value, collections.abc.Mapping):
        value = cls(**{k: value.get(k, None) for k in cls.__dataclass_fields__})
    elif isinstance(value, collections.abc.Sequence) and not isinstance(value, str):
        value = cls(*value)
    else:
        raise TypeError(f"Can not convert '{type(value)}' to dataclass")
        # value = type_hint(value, **kwargs)
    return value


def as_namedtuple(d: dict, name=""):
    return collections.namedtuple(name, d.keys())(d.values())


def as_value(obj: typing.Any) -> HTreeLike:
    if obj is _not_found_ or obj is None:
        return obj
    elif isinstance(obj, collections.abc.Mapping):
        return {k: as_value(v) for k, v in obj.items()}
    elif isinstance(obj, collections.abc.Sequence) and not isinstance(obj, str):
        return [as_value(v) for v in obj]
    elif hasattr(obj.__class__, "__value__"):
        return obj.__value__
    else:
        return obj


def convert_to_named_tuple(d=None, ntuple=None, **kwargs):
    if d is None and len(kwargs) > 0:
        d = kwargs
    if d is None:
        return d
    elif hasattr(ntuple, "_fields") and isinstance(ntuple, type):
        return ntuple(*[try_get(d, k) for k in ntuple._fields])
    elif isinstance(d, collections.abc.Mapping):
        keys = [k.replace('$', 's_') for k in d.keys()]
        values = [convert_to_named_tuple(v) for v in d.values()]
        if not isinstance(ntuple, str):
            ntuple = "__"+("_".join(keys))
        ntuple = ntuple.replace('$', '_')
        return collections.namedtuple(ntuple, keys)(*values)
    elif isinstance(d, collections.abc.MutableSequence):
        return [convert_to_named_tuple(v) for v in d]
    else:
        return d


def get_origin(tp: typing.Any) -> typing.Type:
    """
        获得 object，Type，typing.Generic 的原始类型
    """

    orig_class = typing.get_origin(tp)

    if orig_class is not None:
        return orig_class
    elif inspect.isclass(tp):
        return tp
    else:
        return get_origin(getattr(tp, "__orig_class__", tp.__class__))
        # raise TypeError(f"{tp} must be a class or GenericAlias! {type(tp)}")

    # elif hasattr(tp, "__orig_bases__"):
    #     orig_bases = getattr(tp, "__orig_bases__", None)

    #     if orig_bases is None:
    #         return tp
    #     elif isinstance(orig_bases, tuple):
    #         return get_origin(orig_bases[0])
    #     else:
    #         return get_origin(orig_bases)
    # elif inspect.isclass(tp):
    #     return tp


def get_args(tp: typing.Any) -> typing.Tuple[typing.Type, ...]:
    """
        获得 typing.Generic 类型的 type_hint
        例如： 若定义泛型类
            class Foo[typing.Genric[_T]]:
                pass
            obj=Foo[int]
            get_generic_args(obj)

            >>> int

    """
    if tp is None or tp is _not_found_:
        res = tuple()

    elif isinstance(tp, tuple):
        res = sum([get_args(t) for t in tp], tuple())

    elif typing.get_origin(tp) is not None:
        res = typing.get_args(tp)

    elif inspect.isclass(tp):
        return get_args(getattr(tp, "__orig_bases__", None))

    else:
        return get_args(getattr(tp, "__orig_class__", tp.__class__))

    return tuple([t for t in res if t is not None and not isinstance(t, typing.TypeVar)])


def get_type_hint(tp: typing.Type | types.GenericAlias, prop_name: str):
    if not isinstance(tp, (typing.Type, types.GenericAlias)):
        tp = getattr(tp, "__orig_class__", tp.__class__)

    return typing.get_type_hints(tp).get(prop_name, None)


_T = typing.TypeVar("_T")


def isinstance_generic(obj: typing.Any, type_hint:  typing.Type) -> bool:
    """ 判断 obj 是否是 type_hint 的实例,
        type_hint 可以是 typing.GenericAlias 或者 typing.Type
    """
    if type_hint is None:
        return False

    elif inspect.isclass(type_hint):
        return isinstance(obj, type_hint)

    orig_class = typing.get_origin(type_hint)

    if inspect.isclass(type_hint) and orig_class is None:
        return isinstance(obj, type_hint)
    elif inspect.isclass(type_hint) and obj.__class__ == type_hint:
        return True
    elif orig_class is None:
        # raise RuntimeError(type_hint)
        return False
    elif not isinstance(obj, orig_class):
        return False
    elif getattr(obj, "__orig_class__", obj.__class__) == type_hint:
        return True
    elif not hasattr(obj, "__orig_class__"):
        return True
    elif type_hint in getattr(obj, "__orig_bases__", []):
        return True
    else:
        return False


def type_convert(value: typing.Any, _type_hint: typing.Type,    **kwargs) -> typing.Any:
    if value is _not_found_:
        # raise RuntimeError(f"value is _not_found_")
        return value
    elif _type_hint is None or isinstance_generic(value, _type_hint):
        return value

    if (not inspect.isclass(_type_hint) or not issubclass(_type_hint, (Enum, *primary_type)))\
            and not dataclasses.is_dataclass(_type_hint):

        return _type_hint(value, **kwargs)

    default_value = kwargs.pop("default_value", _not_found_)

    if hasattr(value, "__value__"):
        value = value.__value__

    if value is _not_found_:
        value = default_value

    if value is _not_found_:
        return _not_found_

    origin_class = get_origin(_type_hint)

    if isinstance(value, origin_class):
        pass

    elif issubclass(origin_class, array_type):
        value = as_array(value)

    elif _type_hint in primary_type:
        
        if hasattr(value, "__value__"):
            value = value.__value__

        if value is _not_found_:
            value = kwargs.pop("default_value", _not_found_)

        if value is not _not_found_ and value is not None:
            try:
                tmp = _type_hint(value)
            except Exception as error:
                raise TypeError(f"Can not convert {value} to {_type_hint}") from error
            else:
                value = tmp

    elif dataclasses.is_dataclass(_type_hint):
        value = as_dataclass(_type_hint, value)

    elif issubclass(origin_class, Enum):
        if hasattr(value, "__value__"):
            value = value.__value__
        if isinstance(value, collections.abc.Mapping):
            value = _type_hint[value["name"]]
        elif isinstance(value, str):
            value = _type_hint[value]
        else:
            raise TypeError(f"Can not convert {value} to {_type_hint}")

    else:
        raise TypeError(f"Can not convert {type(value)} to {_type_hint}")

    return value


def convert_to_named_tuple(d=None, ntuple=None, **kwargs):
    if d is None and len(kwargs) > 0:
        d = kwargs
    if d is None:
        return d
    elif hasattr(ntuple, "_fields") and isinstance(ntuple, type):
        return ntuple(*[try_get(d, k) for k in ntuple._fields])
    elif isinstance(d, collections.abc.Mapping):
        keys = [k.replace('$', 's_') for k in d.keys()]
        values = [convert_to_named_tuple(v) for v in d.values()]
        if not isinstance(ntuple, str):
            ntuple = "__"+("_".join(keys))
        ntuple = ntuple.replace('$', '_')
        return collections.namedtuple(ntuple, keys)(*values)
    elif isinstance(d, collections.abc.MutableSequence):
        return [convert_to_named_tuple(v) for v in d]
    else:
        return d


def as_native(d, enable_ndarray=True) -> typing.Union[str, bool, float, int, np.ndarray, dict, list]:
    """
        convert d to native data type str,bool,float, int, dict, list
    """
    if isinstance(d, (bool, int, float, str)):
        return d
    elif isinstance(d, np.ndarray):
        return d.tolist() if not enable_ndarray else d
    elif isinstance(d, collections.abc.Mapping):
        return {as_native(k): as_native(v, enable_ndarray=enable_ndarray) for k, v in d.items()}
    elif isinstance(d, collections.abc.Sequence):
        return [as_native(v, enable_ndarray=enable_ndarray) for v in d]

    else:
        logger.debug(type(d))
        return str(d)


def serialize(obj) -> typing.Any:
    """ 将对象 object serialize 为 native tree结构 （dict,list,np.ndarray,str,bool,int,float)"""

    if obj is None or isinstance(obj, primary_type):
        return obj
    elif isinstance(obj, collections.abc.Mapping):
        return {serialize(k): serialize(v) for k, v in obj.items()}
    elif isinstance(obj, collections.abc.Sequence):
        return [serialize(v) for v in obj]
    elif hasattr(obj, "__serialize__"):
        return obj.__serialize__()
    else:
        raise TypeError(f'Not support type: {type(obj)}')


def dump(obj) -> typing.Any:

    if obj is None or isinstance(obj, primary_type):
        return obj
    elif isinstance(obj, collections.abc.Mapping):
        return {dump(k): dump(v) for k, v in obj.items()}
    elif isinstance(obj, collections.abc.Sequence):
        return [dump(v) for v in obj]
    elif hasattr(obj, "__value__"):
        return dump(obj.__value__)
    else:
        raise TypeError(f'Not support type: {type(obj)}')
