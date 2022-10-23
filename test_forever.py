import os
import signal
import subprocess
import time
from pathlib import Path

BASE_DIR = Path(__file__).absolute().parent


def _pids():
    return sorted(list(BASE_DIR.glob("*.pid")))


def test_forever():
    for i in _pids():
        i.unlink()

    process = subprocess.Popen(["python3", f"{BASE_DIR}/example.py"])
    time.sleep(1.0)
    assert len(_pids()) == 1

    process.kill()
    time.sleep(1.0)
    assert len(_pids()) == 2

    os.kill(int(_pids()[-1].stem), signal.SIGKILL)
    time.sleep(1.0)
    assert len(_pids()) == 3

    subprocess.run(["pkill", "-f", f"{BASE_DIR}/example.py"])
