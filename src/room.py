class Room:
    
    def __init__(self, number):
        self.number = number
        self.guests = []
        self.songs = []

    def check_in(self, guest):
        self.guests.append(guest)

    def check_out(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        
    