# A text adventure game in python
## The setting is my childhood home
### There are classes for player and rooms of the house

### player has attributes 
- name, which is a string
- inventory, which is a list
- location, which is a string

### player has methods
- move, which moves him to a new location
- list inventory
- get inventory item, which allows the player to choose

### room has attributes
- name, which is a string
- stuffstay, which is a list of items that cannot be moved from room
- stuffmove, which is a list of items that can be taken, moved and placed
- adjoining, which is a list of adjoining rooms you can move to
- locked, which is a boolean default set to false
- map, which is a int that points to a ASCII map

### room has methods
- lock_door
- open_door
- look_around, this method seems like is should be a player method by you are actually looking around the room so it is a room method
- get_adjoining, prints a list of adjoining rooms
- get_move-object, prints a list of things you can move

## in edwards_world.py the world is instantiated
here we use the room attributes to create the logic of the rooms
see the code