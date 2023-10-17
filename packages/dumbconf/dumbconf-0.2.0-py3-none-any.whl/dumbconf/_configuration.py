import dumbconf
from dumbconf._namespacing import namespace
import sys
from types import ModuleType
import types
import os
import importlib.util 
import contextlib

def update(config_module: ModuleType, cmds: list[str]):
    target_dict = {
        k: v
        for k, v in vars(config_module).items()
        if isinstance(v, namespace) and not v is namespace
    }

    locals_dict = {}
    with dumbconf.collect_errors() as type_errors:
        for cmd in cmds:
            exec(cmd, target_dict, locals_dict)

    invalid_errors = [
        AttributeError(f"`{key}` does not exist")
        for key, value in locals_dict.items()
    ]

    all_errors = type_errors + invalid_errors

    if len(all_errors) > 0:
        raise ExceptionGroup(
            f"Errors found when updating config '{config_module.__name__}'",
            all_errors,
        )


def save(config_module: ModuleType, filepath: str):
    with open(filepath, "w") as file:
        print("from dumbconf import namespace\n", file=file)
        for obj in vars(config_module).values():
            if isinstance(obj, namespace) and not obj is namespace:
                print(obj, file=file)
                print(file=file)

import importlib.abc

class MyFinder(importlib.abc.MetaPathFinder):
    def __init__(self, filepath: str):
        self.filepath = filepath 

    def find_spec(self, fullname: str, path=None, target=None):
        print("find_spec", fullname, path, target)
        assert (
            not fullname in sys.modules
        ), f"Module `{fullname}` already exists while restoring config. Import your modules *after* calling `dumbconf.load`."
        sys.meta_path.pop(0)
        return importlib.util.spec_from_file_location(
            name=fullname,  # note that ".test" is not a valid module name
            location=self.filepath,
        )

@contextlib.contextmanager
def restore_from(filepath: str):
    assert filepath.endswith(".py"), "Config file must be a python file."
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Config file `{filepath}` does not exist.")
    
    importlib.invalidate_caches()
    sys.meta_path.insert(0, MyFinder(filepath))
    
    yield 

