import sys
from pathlib import Path

from cyla_mixture.backend import Engine
from cyla_mixture.frontend import GUI

if getattr(sys, "frozen", False):
    APP_PATH = Path(getattr(sys, "_MEIPASS"))
elif __file__:
    APP_PATH = Path(__file__).absolute().parent.parent


def main():
    GUI(Engine(), APP_PATH).run()


if __name__ == "__main__":
    main()
