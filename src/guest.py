import pdb

class Guest:
    
    def __init__(self, name, cash, fav_song):
        self.name = name
        self.cash = cash
        self.fav_song = fav_song

    def reduce_cash(self, amount):
        if self.cash >= amount:
            self.cash -= amount

    def check_for_fav_song(self, room):
        for song in room.songs:
            if song == self.fav_song:
                return "Whoo!"