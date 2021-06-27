import unittest

from classes.room import *
from classes.song import *
from classes.guest import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("First", 10, 5)
        self.first_song = Song("Sad But True", "Metallica", "Metal")
        self.songs = [self.first_song]
        self.first_guest = Guest("Juan", 26, 5)
        self.second_guest = Guest("John", 26, 5)
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
# Ask why 1 not 2 since u got 2 in a self.guests. Fixed it no need to ask
    def test_check_in_multiple_guests(self):
        self.room.check_in_multiple_guests(self.guests)
        self.assertEqual(2, self.room.number_of_guests())

    def test_check_out(self):
        self.room.check_in(self.first_guest)
        self.room.check_out(self.first_guest)
        self.assertEqual(0, self.room.number_of_guests())

    def test_room_has_cap(self):
        self.assertEqual(10, self.room.cap)

    def test_rooms_has_entry_fee(self):
        self.assertEqual(5, self.room.fee)



    

