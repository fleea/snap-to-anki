# Utility function to help main function run from project directory
# from project root
# export PYTHONPATH=$PYTHONPATH:.
# This is our python path
import os
import sys
from pathlib import Path

# IS THERE A BETTER WAY?
root_dir = Path(__file__).parent.parent.parent.parent


def get_path(*args: str) -> Path:
    return os.path.join(root_dir, *args)


if __name__ == "__main__":
    print(sys.path)
