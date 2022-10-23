import os
import time
from pathlib import Path

from forever import forever

BASE_DIR = Path(__file__).absolute().parent


def main():
    (BASE_DIR / f"{os.getpid()}.pid").touch()

    for i in range(1000):
        print(f"{i}: hi!")
        time.sleep(2)


if __name__ == "__main__":
    forever(main)
