# Forever

Run the script repeatedly even if the process is killed.

_Note: The script stops only when the child process is killed._

## Example

```python
from forever import forever


def main():
    """do something"""


if __name__ == "__main__":
    forever(main)
```
