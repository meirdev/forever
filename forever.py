import os
from typing import Any, Callable


def forever(fn: Callable[..., Any], *args: Any) -> None:
    read_fd, write_fd = os.pipe()

    # parent
    if os.fork():
        os.close(read_fd)

        fn(*args)

    # child
    else:
        os.setsid()

        os.close(write_fd)

        # wait until parent ending
        os.read(read_fd, 1)

        forever(fn, *args)
