class Song:
    def __init__(self, title, artist_name):
        self.title = title
        self.artist_name = artist_name
        self.songs = []

    def create_song(self, song):
        self.songs.append(song)
