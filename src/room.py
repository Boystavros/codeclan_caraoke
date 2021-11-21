class Room:
    
    def __init__(self, number, max_guests):
        self.number = number
        self.max_guests = max_guests
        self.guests = []
        self.songs = []
        self.entry_fee = 5.00

    def check_in(self, guest):
        if len(self.guests) < self.max_guests:
            self.guests.append(guest)
            return f"Guest {guest.name} added to room {self.number}."
        else:
            return f"Room {self.number} is full, cannot add {guest.name} to room."

    def check_out(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        
    