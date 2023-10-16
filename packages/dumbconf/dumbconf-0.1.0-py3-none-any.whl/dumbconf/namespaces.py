from typing import *
from typing import Any


class _NamespaceMeta(type):
    def __repr__(self) -> str:
        if self.__name__[0].islower():
            repr = f"class {self.__name__}(ns):\n"
            for k, v in self.items():
                repr += f"    {k} = {v}\n"
            # todo handle nested namespaces
            return repr.strip()
        else:
            return super().__repr__()

    def _clean_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    def keys(self):
        return self._clean_dict().keys()

    def values(self):
        return self._clean_dict().values()

    def items(self):
        return self._clean_dict().items()

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.__dict__:
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                f"Attribute `{name}` is not part of namespace `{self.__name__}`"
            )


class ns(metaclass=_NamespaceMeta):
    def __init__(self) -> None:
        raise NotImplementedError("namespaces cannot be instantiated")
