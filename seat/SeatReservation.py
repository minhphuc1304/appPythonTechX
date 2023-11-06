class TreeNode:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.left = None
        self.right = None

class SeatReservationSystem:
    def __init__(self):
        self.root = None
        self.available_seats = set()
    
    def insert_seat(self, seat_number):
        if seat_number not in self.available_seats:
            print(f"Seat {seat_number} is already reserved.")
            return

        self.root = self._insert(self.root, seat_number)
        self.available_seats.remove(seat_number)
        print(f"Seat {seat_number} has been reserved.")

    def _insert(self, node, seat_number):
        if node is None:
            return TreeNode(seat_number)
        
        if seat_number < node.seat_number:
            node.left = self._insert(node.left, seat_number)
        else:
            node.right = self._insert(node.right, seat_number)
        
        return node

    def find_empty_seat(self):
        if not self.root:
            print("All seats are reserved.")
            return None

        current = self.root
        while current.left:
            current = current.left

        empty_seat = current.seat_number
        print(f"An empty seat has been found at seat number {empty_seat}.")
        return empty_seat

    def print_seats_in_order(self):
        if self.root:
            self._print_in_order(self.root)

    def _print_in_order(self, node):
        if node:
            self._print_in_order(node.left)
            print(node.seat_number, end=" ")
            self._print_in_order(node.right)

    def load_seats_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                seat_number = int(line.strip())
                self.insert_seat(seat_number)
                self.available_seats.add(seat_number)
        print("Seats have been loaded from the file.")

    def find_empty_seat(self):
        if not self.root:
            print("All seats are reserved.")
            return None

        current = self.root
        while current.left:
            current = current.left

        empty_seat = current.seat_number
        print(f"An empty seat has been found at seat number {empty_seat}.")
        return empty_seat       

# Example usage:
reservation_system = SeatReservationSystem()

# Load seats from a text file
reservation_system.load_seats_from_file("/Users/lephuc/Desktop/work/seat/seats.txt")

empty_seat = reservation_system.find_empty_seat()