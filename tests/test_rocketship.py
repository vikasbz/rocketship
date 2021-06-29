from django.test import SimpleTestCase

from rocketship import __version__


class TestProject(SimpleTestCase):
    def test_version(self):
        assert __version__ == "0.1.0"
