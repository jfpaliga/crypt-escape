# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

ROOM_ITEMS = {
    "door": "A sturdy oak door locked with a solid padlock",
    "padlock": "A solid steel 4-digit combination lock",
    "casket": "A wooden casket with a slightly rotted lid",
    "book": "An old tome that is sealed with a standard lock",
    "skeleton": '''It's an old skeleton. Something reflects the torchlight 
    from inside it's mouth.'''
}

ITEM_USES = {
    "door": "The door doesn't budge.",
    "casket": "You remove the lid and inside the casket is a skeleton.",
    "book": "The book cannot be opened without a key.",
    "skeleton": "You open the mouth of a skeleton and take a key from inside.",
    "padlock": "Placeholder"
}


class Item:
    def __init__(self, item):
        self.description = ROOM_ITEMS[item]
        self.use = ITEM_USES[item]
        self.is_locked = True

    def describe(self):
        print(self.description)

    def use_object(self):
        print(self.use)


class Player:
    def __init__(self):
        self.inventory = []


def title():
    title = r'''
 _____                  _     _____                         
/  __ \                | |   |  ___|                        
| /  \/_ __ _   _ _ __ | |_  | |__ ___  ___ __ _ _ __   ___ 
| |   | '__| | | | '_ \| __| |  __/ __|/ __/ _` | '_ \ / _ \
| \__/\ |  | |_| | |_) | |_  | |__\__ \ (_| (_| | |_) |  __/
 \____/_|   \__, | .__/ \__| \____/___/\___\__,_| .__/ \___|
             __/ | |                            | |         
            |___/|_|                            |_|         
            '''
    print(title + "\n")
    print("Welcome to Crypt Escape!\n")


def initiate():
    player = Player
    print("You are in a cold stone crypt, a single torch provides light.")
    print("You see a door with a padlock, a closed casket and a book.\n")
    print("To see more details, type examine e.g. 'examine door'")
    print("To use an object, type use e.g. 'use door'")
    print("To see these instructions again, type 'help'\n")
    action = input()
    player_action(player, action)


def examine(item):
    if item in ROOM_ITEMS.keys():
        room_item = Item(item)
        return room_item.describe()
    else:
        print("There is nothing to see.")


def validate_use(player, item):
    if item in ITEM_USES.keys():
        room_item = Item(item)
        return room_item.use_object()
    else:
        print("You cannot use that.")


def player_action(player, action):
    player_input = action.split(' ')

    if player_input[0].lower() == "help":
        initiate()
    elif player_input[0].lower() == "examine":
        examine(player_input[1].lower())
        print("")
        new_action = input()
        player_action(player, new_action)
    elif player_input[0].lower() == "use":
        validate_use(player, player_input[1].lower())
        print("")
        new_action = input()
        player_action(player, new_action)
    else:
        print("Enter a valid input.\n")
        new_action = input()
        player_action(player, new_action)


def main():
    title()
    initiate()


main()
