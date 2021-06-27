class Room:
    def __init__(self, room_name, cap, fee):
        self.room_name = room_name
        self.rooms = []
        self.songs = []
        self.guests = []
        self.cap = cap
        self.fee = fee

    def create_room(self, room):
        self.rooms.append(room)

    def number_of_songs(self):
        return len(self.songs)

    def add_song_to_room(self, song):
        self.songs.append(song)
    
    def number_of_guests(self):
        return len(self.guests)

    def check_in(self, guest):
        self.guests.append(guest)

    def check_in_multiple_guests(self, guests):
        for guest in guests:
            self.check_in(guest)

    def check_out(self, guest):
        self.guests.remove(guest)
