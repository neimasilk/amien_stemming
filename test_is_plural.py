from unittest import TestCase
from amien_stemmer import is_plural


class TestIs_plural(TestCase):
    def test_is_plural(self):
        self.assertEqual(True, is_plural('anak-anak'))
        self.assertEqual(False, is_plural('anak'))
