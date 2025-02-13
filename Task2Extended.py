# room 43 is in butterfly building
import time
import  random

checking={
    30:0,31:0,32:0,33:0,34:0,35:0,36:0,37:0,38:0,39:0,40:0,41:0,42:0,43:0,44:0,45:0,46:0,47:0,48:0,49:0,50:0,51:0,52:0,53:0,54:0,55:0
}

class Vacuum_cleaner:
    def __init__(self,counter,check):
        self.counter=counter
        self.check=check
    def delay(self,time_taken):
        start_time = time.time()
        while time.time() - start_time < time_taken:
            print(".", end="", flush=True)
            time.sleep(0.1)

    def clean_room(self):

        while self.counter>0:
            status_options = ["free", "occupied", "makeup"]
            room_status = {room: random.choice(status_options) for room in range(30, 56)}

            # Define the building structure with floors and rooms
            building = {
                "Firsts floor": {room: random.randint(0, 10) for room in range(30, 36)},
                "Second floor": {room: random.randint(0, 10) for room in range(40, 46)},
                "Third floor": {room: random.randint(0, 10) for room in range(50, 56)}
            }



            self.counter=self.counter-1
            for floor, rooms in building.items():
                print(f"now in {floor}")
                print("now moving in the corridor")
                for room in rooms:
                    # checking if the is occupied or not
                    if room_status[room]=="occupied":
                        print(f"currently the room {room} is occupied based on the data that i do have")
                        print("skipped ............going to the next room it will be cleaned later\n\n")
                        continue
                    print("Moving to room", {room}, end="", flush=True)
                    self.delay(2)

                    # checking if the room is having a makeup class or not
                    if room_status[room]=="makeup":
                        print(f"currently the room {room} is having a makeup class")
                        print("skipped ............going to the next room it will be cleaned later\n\n")
                        continue
                    print(f"Checking Room {room}........")
                    if rooms[room]!=0:
                        print(f"room {room} is dirty")
                        time_taken = building[floor][room]
                        print("now cleaning room",{room}, end="", flush=True)
                        self.delay(time_taken)
                        print(f"\n\nThe agent has spent {time_taken} seconds cleaning room {room}")
                        # rooms[room]=""
                        self.check[room]+=1
                        print(f"room {room} is now cleaned")
                        print(f"Now moving out of room {room} into the corridor", end="", flush=True,)


                    else:
                        print(f"room {room} is clean")
                        print(f"Now moving out of room {room} into the corridor")
                    print("Now moving in the corridor≥≥≥≥≥≥≥≥≥≥≥...............\n\n")

                print("============================================================================================================================================================")
    def most_likely(self):
        larger=self.check[30]
        keptroom = []
        for room in self.check:
            if larger < self.check[room]:
                larger = self.check[room]
        #         checking all room that are the dirtiest
        for room in checking:
            if checking[room] == larger:
                keptroom.append(room)
        print(f"the room which is most likely to be dirty is {keptroom}")


Vacuum=Vacuum_cleaner(3,checking)
Vacuum.clean_room()
Vacuum.most_likely()
