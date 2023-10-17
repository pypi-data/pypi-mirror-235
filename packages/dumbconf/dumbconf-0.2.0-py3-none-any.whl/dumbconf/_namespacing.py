import contextlib
from typing import *
from inspect import isclass


class _NamespaceMeta(type):
    def __repr__(self, indent=1) -> str:
        if self.__name__[0].islower():
            result = f"class {self.__name__}({', '.join(x.__name__ for x in self.__bases__)}):\n"

            if len(self) == 0:
                result += f"{4*indent*' '}pass\n"
            else:
                for k, v in self.items():
                    if isinstance(v, namespace):
                        result += f"{4*indent*' '}{_NamespaceMeta.__repr__(v, indent=indent + 1)}"
                    else:
                        result += f"{4*indent*' '}{k} = {repr(v)}\n"

            return result.strip()
        else:
            return super().__repr__()

    def __len__(self) -> int:
        return len(self._clean_dict())

    def _clean_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    def keys(self):
        return self._clean_dict().keys()

    def values(self):
        return self._clean_dict().values()

    def items(self):
        return self._clean_dict().items()

    def __setattr__(self, name: str, value: Any) -> None:
        if self.__name__[0].islower():
            if name in self.__dict__:
                if name in self.__annotations__:
                    expected_type = self.__annotations__[name]
                else:
                    expected_type = type(self.__dict__[name])

                check_type(name, value, expected_type, self)
                super().__setattr__(name, value)
                # todo set the error message to the correct line
            else:
                attrib_error = AttributeError(
                    f"`{self.__name__}.{name}` does not exist"
                )
                if _collected_errors is not None:
                    _collected_errors.append(attrib_error)
                else:
                    raise attrib_error
        else:
            super().__setattr__(name, value)

    def __instancecheck__(self, instance):
        return isclass(instance) and namespace in instance.__mro__

class namespace(metaclass=_NamespaceMeta):
    def __init__(self) -> None:
        if self.__class__.__name__[0].islower():
            raise NotImplementedError(f"Namespaces cannot be instantiated (to to instantiate '{self.__class__.__name__}')")
        else:
            super().__init__()

    def __init_subclass__(cls) -> None:  # ? does this work with subclassing
        for name in cls.__annotations__:
            if name in cls.__dict__:
                value = cls.__dict__[name]
                expected_type = cls.__annotations__[name]
                check_type(name, value, expected_type, cls)
                # todo set the error message to the correct line


_collected_errors = None


@contextlib.contextmanager
def collect_errors():
    global _collected_errors
    _tmp = _collected_errors
    _collected_errors = []
    yield _collected_errors
    _collected_errors = _tmp

from inspect import currentframe
import inspect

def check_type(name, value, expected_type, ns):
    if not isinstance(value, expected_type) or (type(value) == bool and expected_type == int) or (type(value) == int and expected_type == bool): # in Python bool is a subclass of int...
        type_error = TypeError(
            f"`{ns.__name__}.{name}` must be of type '{expected_type.__name__}', not '{type(value).__name__}'"
        )
        if _collected_errors is not None:
            _collected_errors.append(type_error)
        else:

            if _collected_errors is None:
                frame = currentframe().f_back.f_back
                source = inspect.getsource(frame.f_code)
                k = source.find(name)
                k2 = source.find('\n', k)
                type_error.add_note(f"The error occured with definition `{source[k:k2].strip()}` in file {frame.f_code.co_filename}:{frame.f_lineno}")
            raise type_error

