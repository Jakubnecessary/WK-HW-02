class Guest:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.guests = []

    def create_guest(self, guest):
        self.guests.append(guest)


    