import unittest

from classes.room import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1)

    def test_room_has_number(self):
        self.assertEqual(1, self.room.room_number)