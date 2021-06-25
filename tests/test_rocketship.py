import django

from rocketship import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_django():
    print(f"Django version: {django.__version__}")


if __name__ == "__main__":
    test_version()
    test_django()
