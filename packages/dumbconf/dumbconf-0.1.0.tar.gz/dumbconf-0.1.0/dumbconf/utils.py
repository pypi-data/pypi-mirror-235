import os
import contextlib
from datetime import datetime
import shutil


@contextlib.contextmanager
def directory(path: str, delete_if_exists: bool = False):
    if not os.path.exists(path):
        if delete_if_exists:
            shutil.rmtree(path)
        os.makedirs(path, exist_ok=True)
    with contextlib.chdir(path):
        yield path


def timestamp():
    return datetime.now().isoformat(timespec="seconds")  # todo windows format
