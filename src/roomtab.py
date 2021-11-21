class RoomTab:

    def __init__(self, room_num):
        self.room_num = room_num
        self.guests = 0
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
        
    def increase_guests_on_tab(self):
        self.guests += 1
