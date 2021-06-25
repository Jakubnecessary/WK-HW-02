import unittest

from classes.song import *


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Sad But True", "Metallica")

    def test_song_has_title(self):
        self.assertEqual("Sad But True", self.song.title)

    def test_song_has_artist_name(self):
        self.assertEqual("Metallica", self.song.artist_name)