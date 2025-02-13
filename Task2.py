# room 43 is in butterfly building
import time
import  random

ButterFly={
    "Firsts floor":{30:"*********",31:"**",32:"****",33:"",34:"*",35:"******"},
    "Second floor":{40:"",41:"",42:"***",43:"***********",44:"*",45:"*"},
    "Third floor":{50:"**********",51:"",52:"",53:"",54:"",55:"***"}
}

# Possible values
status_options = ["free", "occupied", "makeup"]

# Generate the dictionary with random values
room_status = {room: random.choice(status_options) for room in range(30, 56)}


class Vacuum_cleaner:
    def __init__(self,building):
        self.building=building

    def delay(self,time_taken):
        start_time = time.time()
        while time.time() - start_time < time_taken:
            print(".", end="", flush=True)
            time.sleep(0.1)

    def clean_room(self):
        for floor, rooms in self.building.items():
            print(f"now in {floor}")
            print("now moving in the corridor")
            for room in rooms:
                # checking if the is occupied or not
                if room_status[room]=="occupied":
                    print(f"currently the room {room} is occupied based on the timetable")
                    print("skipped ............going to the next room it will be cleaned later")
                    continue
                print("Moving to room", {room}, end="", flush=True)
                self.delay(2)

                # checking if the room is having a makeup class or not
                if room_status[room]=="makeup":
                    print(f"currently the room {room} is having a makeup class")
                    print("skipped ............going to the next room it will be cleaned later")
                    continue
                print(f"Checking Room {room}........")
                if rooms[room]!="":
                    print(f"room {room} is dirty")
                    time_taken = ButterFly[floor][room].count("*")
                    print("now cleaning room",{room}, end="", flush=True)
                    self.delay(time_taken)
                    rooms[room]=""
                    print(f"room {room} is now cleaned")
                    print(f"Now moving out of room {room} into the corridor", end="", flush=True,)

                else:
                    print(f"room {room} is clean")
                    print(f"Now moving out of room {room} into the corridor")
                print("Now moving in the corridor≥≥≥≥≥≥≥≥≥≥≥...............\n\n")
            print("============================================================================================================================================================")


Vacuum=Vacuum_cleaner(ButterFly)
Vacuum.clean_room()
