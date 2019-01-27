

class Room:
    """ room class for describing 2015 Edwards in a adventure type game """
    def __init__(self):
        self.name = ""
        self.stuffStay = []
        self.stuffMove = []
        self.adjoining = []
        self.locked = False
        self.map = 0

        
    def __str__(self):
        return self.name
    
    def lock_door(self):       # can lock and unlock
        self.locked = True
        return "this room is locked"
        
    def open_door(self):
        self.locked = False
        return "this room is now open"
    
    def look_around(self):
        print()
        print("*"*30)
        print("You are at {}.".format(self.name))
        print()
        print("You can see:")
        for num, item in enumerate(self.stuffStay,1):
            print("\t" + str(num), str(item))
        print()
        print("You can take:")
        for num, item in enumerate(self.stuffMove,1):
            print("\t" + str(num), str(item))    
        print()
        print("You can go:")
        for num, room in enumerate(self.adjoining,1):
            print("\t" + str(num), str(room))
            
    def get_adjoining(self):
        print("You can go:")
        for num, room in enumerate(self.adjoining,1):
            print("\t" + str(num), str(room))
        answer = 0
        while answer not in list(range(1,len(self.adjoining)+1)):
            try:
                str_answer = input("Enter the number of the room: ")
                answer = int(str_answer)
            except ValueError:
                print("that is not a number")
        return answer-1 

    def get_move_object(self):
        print("You can take:")
        for num, room in enumerate(self.stuffMove,1):
            print("\t" + str(num), str(room))
        answer = 0
        while answer not in list(range(1,len(self.stuffMove)+1)):
            try:
                str_answer = input("Enter the number of the item: ")
                answer = int(str_answer)
            except ValueError:
                print("that is not a number")
        return answer-1 

            
## get_adjoining and get move object  will return a number of the index of the room that can be moved to or thing to be taken
     
## second floor         
    
kitchen_f2 = Room()
kitchen_f2.name = "second floor kitchen"
kitchen_f2.stuffStay = ["stove", "oven","fridge","table","wall phone with cord", "radiator"]
kitchen_f2.stuffMove = ["pen","apple"]
kitchen_f2.map = 1

back_bedroom_f2 =Room()
back_bedroom_f2.name = "second floor back bedroom"
back_bedroom_f2.stuffStay = ["trundle bed","toy shelf","record player", "dresser"]
back_bedroom_f2.stuffMove = ["G.I. Joe", "book"]
back_bedroom_f2.map =1

back_porch_f2 = Room()
back_porch_f2.name = "second floor back porch"
back_porch_f2.stuffStay = ["bucket","folding chair", "back yard below", "shed"]
back_porch_f2.map = 1

bathroom_f2 = Room()
bathroom_f2.name = "second floor bathroom"
bathroom_f2.stuffStay = ["cast-iron tub with feet", "toilet", "sink", "mirror"]
bathroom_f2.map =1

living_room_f2 = Room()
living_room_f2.name = "second floor living room"
living_room_f2.stuffStay = ["green couch", "box television", "reclining chair", "square brown carpet", "book case with National Graphics and encyclopedia"]
living_room_f2.map =1

front_bedroom_f2 = Room()
front_bedroom_f2.name = "second floor front bedroom"
front_bedroom_f2.stuffStay = ["French doors with white curtains", "queen size bed", "dresser", "mirror", "jewelry box"]
front_bedroom_f2.map =1 

front_porch_f2 = Room()
front_porch_f2.name = "second floor front porch"
front_porch_f2.stuffStay =["concrete pillars and black metal railing", "folding chair", "Edwards street below","sausage factory opposite","electric lines suspended between wooden polls"]
front_porch_f2.map = 1

## linking stairs
back_porch_stairs = Room()
back_porch_stairs.name = "back porch stairs"

## first floor
kitchen_f1 = Room()
kitchen_f1.name = "first  floor kitchen"
kitchen_f1.stuffStay = ["stove", "oven","fridge","table", "radiator"]
kitchen_f1.map =2

back_bedroom_f1 =Room()
back_bedroom_f1.name = "first  floor back bedroom"
back_bedroom_f1.stuffStay = ["grand parent's bed", "sewing machine", "desk", "black telephone", "dresser with mirror"]
back_bedroom_f1.map = 2

back_porch_f1 = Room()
back_porch_f1.name = "first  floor back porch"
back_porch_f1.stuffStay = ["bucket","folding chair", "back yard below", "shed"]
back_porch_f1.map =2

bathroom_f1 = Room()
bathroom_f1.name = "first  floor bathroom"
bathroom_f1.stuffStay = ["cast-iron tub with feet", "toilet", "sink", "mirror"]
bathroom_f1.map =2

living_room_f1 = Room()
living_room_f1.name = "first floor living room"
living_room_f1.stuffStay = ["brown couch", "box television", "rocking char", "square brown carpet","front door"]
living_room_f1.map =2

front_bedroom_f1 = Room()
front_bedroom_f1.name = "first  floor front bedroom"
front_bedroom_f1.stuffStay = ["wooden French doors", "two single beds", "dresser", "mirror", "make-up table"]
front_bedroom_f1.map =2

front_porch_f1 = Room()
front_porch_f1.name = "first floor front porch"
front_porch_f1.stuffStay =["concrete pillars and black metal railing", "Edwards street","sausage factory opposite"]
front_porch_f1.map =2
## linking stairs

yard_stairs = Room()
yard_stairs.name = "concrete yard stairs"

## yard

concrete_patch = Room()
concrete_patch.name = "concrete patch in the back yard"
concrete_patch.map = 4

grass_patch = Room()
grass_patch.name = "grass patch in the back yard"
grass_patch.map =4

shed = Room()
shed.name = "brick shed"
shed.map = 4

## linking stairs
outside_basement_stairs = Room()
outside_basement_stairs.name = "outside basement stairs"

## basement
large_room_b = Room()
large_room_b.name = "basement large room"
large_room_b.map = 3

workshop_b = Room()
workshop_b.name = "Grandpa's workshop "
workshop_b.map = 3

toilet_b = Room()
toilet_b.name = "basement toilet"
toilet_b.map =3
## linking stairs

basement_stairs = Room()
basement_stairs.name = "wooden stairs to the basement"





# moved adjoining to after all have been instantiated
# this is the logic of the Edwards layout

## second floor
kitchen_f2.adjoining = [back_bedroom_f2,back_porch_f2,living_room_f2, bathroom_f2]
back_bedroom_f2.adjoining = [kitchen_f2]
back_porch_f2.adjoining = [kitchen_f2,back_porch_stairs]
bathroom_f2.adjoining =[kitchen_f2,living_room_f2]
living_room_f2.adjoining = [kitchen_f2,front_bedroom_f2,bathroom_f2,front_porch_f2]
front_bedroom_f2.adjoining =[living_room_f2,front_porch_f2]
front_porch_f2.adjoining = [living_room_f2,front_bedroom_f2]

## linking stairs
back_porch_stairs.adjoining = [back_porch_f2,back_porch_f1]

## first floor
kitchen_f1.adjoining = [back_bedroom_f1,back_porch_f1,living_room_f1, bathroom_f1]
back_bedroom_f1.adjoining = [kitchen_f1,basement_stairs]
back_porch_f1.adjoining = [kitchen_f1,back_porch_stairs,yard_stairs]
bathroom_f1.adjoining =[kitchen_f1,living_room_f1]
living_room_f1.adjoining = [kitchen_f1,front_bedroom_f1,bathroom_f1,front_porch_f1]
front_bedroom_f1.adjoining =[living_room_f1,front_porch_f1]
front_porch_f1.adjoining = [living_room_f1,front_bedroom_f1]

## linking stairs
yard_stairs.adjoining = [back_porch_f1,concrete_patch]

## yard
concrete_patch.adjoining = [yard_stairs,grass_patch]
grass_patch.adjoining =[concrete_patch,shed]
shed.adjoining = [grass_patch]

## linking stairs
outside_basement_stairs.adjoining = [concrete_patch, large_room_b]
basement_stairs.adjoining = [workshop_b,back_bedroom_f1]
## basement

large_room_b.adjoining = [outside_basement_stairs, workshop_b, toilet_b]

toilet_b.adjoining = [large_room_b]

workshop_b.adjoining = [large_room_b, basement_stairs]


## maybe just have a class room instead of kitchen and put the logic of connected room after instantiating

## you can check you check if you can go to the room if destination room is in room.adjoining list

