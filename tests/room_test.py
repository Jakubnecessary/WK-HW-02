import unittest

from classes.room import *
from classes.song import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("First")
        self.first_song = Song("Sad But True", "Metallica", "Metal")
        self.songs = [self.first_song]

    def test_room_has_name(self):
        self.assertEqual("First", self.room.room_name)

    def test_create_rooms(self):
        self.room.create_room(self.room)
        self.assertEqual("First", self.room.room_name)

    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.first_song)
        self.assertEqual(1, self.room.number_of_songs())
