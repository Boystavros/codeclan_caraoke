from src.roomtab import RoomTab

class Room:
    
    def __init__(self, number, max_guests):
        self.number = number
        self.max_guests = max_guests
        self.guests = []
        self.songs = []
        self.room_tab = RoomTab(number) 
        
    def check_in(self, guest):
        if len(self.guests) < self.max_guests:
            self.guests.append(guest)
            self.room_tab.increase_guests_on_tab()
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

    def sell_drink(self, price):
        self.room_tab.add_drink_cost_to_bill(price)

    def retrieve_bill(self):
        return self.room_tab.calculate_bill()

    def charge_amount(self, amount):
        self.room_tab.reduce_bill(amount)
