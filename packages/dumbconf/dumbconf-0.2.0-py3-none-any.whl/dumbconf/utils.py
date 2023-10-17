import os
import contextlib
from datetime import datetime
from dateutil.tz import tzlocal
import shutil


@contextlib.contextmanager
def directory(path: str, delete_if_exists: bool = False):
    if path not in ["", ".", "./"] and not path.isspace():
        if not os.path.exists(path):
            if delete_if_exists:
                shutil.rmtree(path)
            os.makedirs(path, exist_ok=True)
        with contextlib.chdir(path):
            yield path
    else:
        yield path


def timestamp():
    return (
        datetime.now(tzlocal())
        .isoformat(timespec="seconds")
        .replace(":", "h", 1)
        .replace(":", "m", 1)
        .replace("+", "s+", 1)
        .removesuffix(":00")
    )


def imopen(path):
    from PIL import Image
    from torchvision.transforms.functional import to_tensor

    return to_tensor(Image.open(path))[None]


def imsave(image, path, **kwargs):
    from torchvision.utils import save_image

    with directory(os.path.dirname(path)):
        save_image(image, path, **{"padding": 0, **kwargs})
