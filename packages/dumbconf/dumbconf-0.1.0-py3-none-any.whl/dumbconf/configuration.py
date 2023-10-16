import sys
from dumbconf.namespaces import ns
from types import ModuleType
import runpy
import tempfile
import shutil
from inspect import isclass
import types
import os
import importlib


def update(config_module_or_ns: ModuleType | ns, cmds: list[str] | str = sys.argv[1:]):
    if isinstance(cmds, str):
        cmds = [cmds]

    if isinstance(config_module_or_ns, ns):
        target_dict = {ns.__name__: config_module_or_ns}
    else:
        target_dict = {
            k: v
            for k, v in vars(config_module_or_ns).items()
            if isclass(v) and issubclass(v, ns) and not v is ns
        }

    for cmd in cmds:
        exec(cmd, target_dict)


def save(config_module: ModuleType, filepath: str):
    with open(filepath, "w") as file:
        print("from dumbconf.namespaces import ns\n", file=file)
        for obj in vars(config_module).values():
            if isclass(obj) and issubclass(obj, ns) and not obj is ns:
                print(obj, file=file)
                print(file=file)


def restore(config_module_qualname: str, filepath: str):
    # todo must pretend we are executing as a module while running
    assert (
        not config_module_qualname in sys.modules
    ), f"Module `{config_module_qualname}` already exists while restoring config. Import your modules *after* calling `dumbconf.restore`."

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Config file `{filepath}` does not exist.")

    module = types.ModuleType(config_module_qualname)
    exec(open(filepath).read(), module.__dict__)
    sys.modules[config_module_qualname] = module
    # assert __import__(config_module_qualname)
    # try:
    #     importlib.util.find_spec(config_module_qualname)
    # # to make sure the module qualnaem is correct, try to import it. But, this must be done *after* the restore.
    # except ValueError:
    #     raise ValueError(
    #         f"The config module `{config_module_qualname}` does not exists/could not be found."
    #     )
    # sys.modules[config_module_qualname] = module
