import edwards_world

class Player:
    def __init__(self):
        self.name = ""
        self.inventory = [ ]
        self.location = ""
    
    def __str__(self):
        return self.name
    
    
    def where(self):
        return self.location
    
    def move(self,new_location):
        self.location = new_location
        #print("you are now in: ", new_location)
        new_location.look_around()
        
    def list_inventory(self):
        
        print("I have:")
        for num, item in enumerate(self.inventory,1):
            print("\t" + str(num), str(item))

    def get_inventory_item(self):
        print("You can choose:")
        for num, room in enumerate(self.inventory,1):
            print("\t" + str(num), str(room))
        answer = 0
        while answer not in list(range(1,len(self.inventory)+1)):
            try:
                str_answer = input("Enter the number of the item: ")
                answer = int(str_answer)
            except ValueError:
                print("that is not a number")
        return answer-1         
        
        


    
        
##greg = Player()
##greg.name = "Gregory Kreisman"
##greg.location = edwards_world.kitchen_f2
##greg.inventory = ["record","sandwich","magnifying glass"]

##  the move works this way greg.location is instantiated then we use current pointers with the room attributes like adjoining
##greg.move(greg.location.adjoining[0])
##you are now in:  second floor back bedroom
##>>> print(greg.location)
##second floor back bedroom
##>>> greg.move(greg.location.adjoining[0])
##you are now in:  second floor kitchen
##>>>

##>>> greg.location.look_around()
##You are at second floor kitchen.
##You can see:
##  1 stove
##  2 oven
##  3 fridge
##  4 table
##  5 wall phone with cord
##You can go:
##  1 second floor back bedroom
##  2 second floor back porch
##  3 second floor living room
##>>> greg.move(greg.location.adjoining[1])
##you are now in:  second floor back porch
##You are at second floor back porch.
##You can see:
##  1 bucket
##  2 folding chair
##You can go:
##  1 second floor kitchen