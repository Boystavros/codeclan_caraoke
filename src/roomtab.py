class RoomTab:

    def __init__(self, room_num):
        self.room_num = room_num
        self.guests = 0
        self.entry_fee = 5.00
        self.bill = []
        self.bill_total = 0

    def total_entry_fees(self):
        return self.entry_fee * self.guests

    def add_drink_cost_to_bill(self, cost):
        self.bill.append(cost)
        self.bill_total += cost

    def total_drinks_bill(self):
        return self.bill_total

    def calculate_bill(self):
        return self.total_entry_fees() + self.bill_total
        
    def increase_guests_on_tab(self):
        self.guests += 1

    def reduce_bill(self, amount):
        if self.bill_total >= amount:
            self.bill_total -= amount
        elif (self.bill_total + self.entry_fee) >= amount:
            self.entry_fee -= amount - self.bill_total
            self.bill_total == 0.00
