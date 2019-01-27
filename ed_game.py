from edplayer import Player
import edwards_world


def map_second_floor():
    print("""
     
                   Second Floor                     
        ---------------------------------------     
     B  |               |b| |                  |F   
     a  | back bedroom  |c|f|   front bedroom  |r   
     c P|               | |c|                   o P 
     k o|------  -------------------  ---------|n o 
       r|                                      |  r 
     = c   kitchen      |Ba |   living rooom      c 
     = h|               |Ro |                  |  h 
     =  ---------------------------------------     
    """)

def map_first_floor():
    print("""
     
                    First Floor                    
        ---------------------------------------    
     B  |            ||||b| |                  |F  
     a  | back bedroom  |c|f|   front bedroom  |r  
     c P|               | |c|                  |o P
     k o|------  -------------------  ---------|n o 
       r|                                      |  r 
     = c   kitchen      |Ba |   living rooom      c 
     = h|               |Ro |                  |  h 
     =  ---------------------------------------     
     """)

def map_basement():
    print("""
     
                     Basement                 
       ---------------------------------------
     B | toilet|  furnace   ||||              |
     a |-------- -----------      work room   |
     c ||||                   |               |
     k |                      |---------------|
       |      front rooom                     |
       |                                      |
       |                                      |
        -------------------------------------- 
    """)    


def map_yard():


    print( """
         
                            Yard                  
            -------------------------------------  |
         B  |      |         |                  |  |
         r  | shed |         |                  |p |
         i W|      |         |    concrete      |o | 
         c a|-------         |      patch       |r | 
         k l|      grass     |                  |c | 
           l|       patch    |              |||||h | 
            |                |                  |  _
            ------------------------------------- 
    """)


def get_player_command():
    print()
    print()
    return input('Action: ')

def play():
    print ("Welcome Back to 2015 Edwards, your childhood home")
    print ()
    print("""
/______________________/|
|^^^^^^^^^^^^^^^^^^^^^^||
|-----------------------|
| [ ] | |    | | [ ]   || 
|-----| |----| |------ ||
|+ + +| |+ + | | + + + ||
|______________________||
|^^^^^^^^^^^^^^^^^^^^^^||
|----------------------||
| [ ] | |    | | [ ]   || 
|-----| |----| |-------||
|+ + +| |+ + | | + + + || 
[][][][][][][][][][][][]]
[][][][][][][][][][][][]]

    """)
    greg = Player()
    greg.name = "Gregory Kreisman"
    greg.location = edwards_world.kitchen_f2
    greg.inventory = ["record","sandwich","magnifying glass"]
     
    keep_play = True
    while keep_play:
        
        action_input = get_player_command()
        if action_input in ['goto', 'go to', 'move', 'go']:
            print("I will move")
            print()
            choice = greg.location.get_adjoining() #directs to method from edwards_world that returns an index of the choice from list of adjoining rooms 
            #print(choice)
            #print(greg.location.adjoining[choice]) # choice is the index and is the data in the list of adjoining rooms set in edwards_world
            greg.move(greg.location.adjoining[choice]) #calls the method from edplayer that moves from one locatin to another
             
        elif action_input in ['take', 'get']:
            if len(greg.location.stuffMove) > 0:
                #print("I will take")
                print()
                choice = greg.location.get_move_object()
                #print(choice)
                #print(greg.location.stuffMove[choice])
                greg.inventory.append(greg.location.stuffMove[choice])
                greg.location.stuffMove.pop(choice)
                print()
                print("got it!")
            else:
                print("There is nothing here you can take")
                print()    

        elif action_input in ["drop","put down", "leave"]:
            if len(greg.inventory) > 0:         ## needed to make sure that there is sometheing to drop
                #print("I will drop")
                print()
                choice = greg.get_inventory_item()
                #print(choice)
                #print(greg.inventory[choice]) 
                greg.location.stuffMove.append(greg.inventory[choice])
                greg.inventory.pop(choice)
                print()
                print("dropped it!")
            else:
                print("You have nothing to drop!")
                print()       



        elif action_input in ['look around', 'look']:
            print("I am looking around")
            print("*"*30)
            greg.location.look_around()
         
        elif action_input in ['who am I', 'me', 'who am i']:
            print()
            print("*"*30)
            print(greg.name)
            print()
         
        elif action_input in ['m', 'map']:
            print()
            print()
            if greg.location.map == 4:
                map_yard()
            elif greg.location.map == 1:
                map_second_floor()
            elif greg.location.map == 2:
                map_first_floor()
            elif greg.location.map == 3:
                map_basement()        
            else:
                print("no map here!")    

        
        elif action_input in ['i', 'i', 'inventory', 'have']:
            print()
            print()
            greg.list_inventory()
        
        elif action_input in ['q', 'Q', 'quit']:
            keep_play = False           
        else:
            print("*"*30)
            print("Invalid action!")    


        

         
           
    
play()

