import unittest

from classes.room import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1)

    def test_room_has_number(self):
        self.assertEqual(1, self.room.room_number)

    def test_create_rooms(self):
        self.room.create_room(self.room)
        self.assertEqual(1, self.room.room_number)
