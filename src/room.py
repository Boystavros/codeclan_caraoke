class Room:
    
    def __init__(self, number):
        self.number = number
        self.guests = []
        self.songs = []

    def check_in(self, guest):
        self.guests.append(guest)