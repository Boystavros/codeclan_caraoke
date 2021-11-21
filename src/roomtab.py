class RoomTab:

    def __init__(self, room):
        self.room = room
        self.bill = []

    def total_entry_fees(self):
        return self.room.entry_fee * len(self.room.guests)

    def add_drink_cost_to_bill(self, cost):
        self.bill.append(cost)

    def total_drinks_bill(self):
        return sum(self.bill)

    def calculate_bill(self):
        return self.total_entry_fees() + self.total_drinks_bill()
        