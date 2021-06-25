class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.rooms = []

    def create_room(self, room):
        self.rooms.append(room)