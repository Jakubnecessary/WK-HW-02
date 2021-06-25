import unittest

from classes.guest import *


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Juan", 26)

    def test_guest_has_name(self):
        self.assertEqual("Juan", self.guest.name)