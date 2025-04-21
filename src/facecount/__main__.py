import os, sys

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from facecount.facecount import facecount

def main():
    try:
        facecount()
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())
