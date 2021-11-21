class RoomTab:

    def __init__(self, room_num, num_guests):
        self.room_num = room_num
        self.guests = num_guests
        self.entry_fee = 5.00
        self.bill = []

    def total_entry_fees(self):
        return self.entry_fee * self.guests

    def add_drink_cost_to_bill(self, cost):
        self.bill.append(cost)

    def total_drinks_bill(self):
        return sum(self.bill)

    def calculate_bill(self):
        return self.total_entry_fees() + self.total_drinks_bill()
        