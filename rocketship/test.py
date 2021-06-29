from django import __version__
from django.test import SimpleTestCase


class TestDjango(SimpleTestCase):
    def test_django_version(self):
        assert __version__ == "3.2.4"
