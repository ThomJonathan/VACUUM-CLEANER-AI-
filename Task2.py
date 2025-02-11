# room 43 is in butterfly building
import time

ButterFly={
    "Firsts floor":{30:"clean",31:"dirty",32:"dirty",33:"clean",34:"dirty",35:"clean"},
    "Second floor":{40:"clean",41:"clean",42:"dirty",43:"dirty",44:"dirty",45:"dirty"},
    "Third floor":{50:"dirty",51:"clean",52:"clean",53:"clean",54:"clean",55:"dirty"}
}

class Vacuum_cleaner:
    def __init__(self,building):
        self.building=building

    def delay(self):
        start_time = time.time()
        while time.time() - start_time < 3:
            print(".", end="", flush=True)
            time.sleep(0.1)

    def clean_room(self):
        for floor, rooms in self.building.items():
            print(f"now in {floor}")
            print("now moving in the corridor")
            for room in rooms:
                print("Moving to room", {room}, end="", flush=True)
                self.delay()

                print(f"Checking Room {room}........")
                if rooms[room]=="dirty":
                    print(f"room {room} is dirty")
                    rooms[room]="clean"

                    print("now cleaning room",{room}, end="", flush=True)
                    self.delay()
                    print(f"room {room} is now cleaned")
                    print(f"Now moving out of room {room} into the corridor", end="", flush=True,)

                else:
                    print(f"room {room} is clean")
                    print(f"Now moving out of room {room} into the corridor")
                print("Now moving in the corridor≥≥≥≥≥≥≥≥≥≥≥...............\n\n")
            print("============================================================================================================================================================")


Vacuum=Vacuum_cleaner(ButterFly)
Vacuum.clean_room()
