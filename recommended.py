# TASK 1 EXTENDED
from datetime import time
import time

class Vacuum_cleaner:
    def __init__(self, rooms):
        self.rooms = rooms

    def roomA(self):

        print("now in Room A")
        print("Checking Room A")
        if self.rooms["A"] == "dirty":
            print("Room A is dirty")
            self.rooms["A"] = "clean"
            print("Room A is cleaned")

        else:
            print("Room A is clean")
        print("Moving to room B", end="", flush=True)
        start_time = time.time()
        while time.time() - start_time < 1:
            print(".", end="", flush=True)
            time.sleep(0.1)

    def roomB(self):

        print("now in Room B")
        print("Checking Room B")
        if self.rooms["B"] == "dirty":
            print("Room B is dirty")
            self.rooms["B"] = "clean"
            print("Room B is cleaned")

        else:
            print("Room B is clean")
        # move_right()
        print("Moving to room A", end="", flush=True)
        start_time = time.time()
        while time.time() - start_time < 1:
            print(".", end="", flush=True)
            time.sleep(0.1)


room= {"A": "", "B": ""}
# Read file and update dictionary
with open('/Users/mac/Desktop/THOM/ARTIFICIAL INTELLIGENCE/vacuum.txt', 'r') as file:
    for line in file:
        sta1, sta2 = line.strip().split(", ")
        room["A"],room["B"]=sta1,sta2
        Vacuum=Vacuum_cleaner(room)
        Vacuum.roomA()
        Vacuum.roomB()


