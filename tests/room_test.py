import unittest

from classes.room import *
from classes.song import *
from classes.guest import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("First")
        self.first_song = Song("Sad But True", "Metallica", "Metal")
        self.songs = [self.first_song]
        self.first_guest = Guest("Juan", 26)
        self.second_guest = Guest("John", 26)
        self.guests = [self.first_guest, self.second_guest]

    def test_room_has_name(self):
        self.assertEqual("First", self.room.room_name)

    def test_create_rooms(self):
        self.room.create_room(self.room)
        self.assertEqual("First", self.room.room_name)

    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.first_song)
        self.assertEqual(1, self.room.number_of_songs())

    def test_check_in_single(self):
        self.room.check_in(self.first_guest)
        
        self.assertEqual(1, self.room.number_of_guests())
# Ask why 1 not 2 since u got 2 in a self.guests.
    def test_check_in_multiple_guests(self):
        self.room.check_in(self.guests)
        self.assertEqual(1, self.room.number_of_guests())

    

