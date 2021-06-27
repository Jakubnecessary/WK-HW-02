class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self.rooms = []
        self.songs = []

    def create_room(self, room):
        self.rooms.append(room)

    def number_of_songs(self):
        return len(self.songs)

    def add_song_to_room(self, song):
        self.songs.append(song)