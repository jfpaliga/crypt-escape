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
    "locked door": "The door doesn't budge.",
    "unlocked door": "The door swings open, revealing the way out!",
    "casket": "You remove the lid and inside the casket is a skeleton.",
    "locked book": "The book cannot be opened without a key.",
    "unlocked book": "The lock comes free allowing you to read the book.",
    "skeleton": "You open the mouth of a skeleton and take a key from inside."
}


class Item:
    def __init__(self, item):
        self.description = ROOM_ITEMS[item]
        self.use = None

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
    print("You are in a cold stone crypt, a single torch provides light.")
    print("You see a door with a padlock, a closed casket and a book.\n")
    print("To see more details, type examine e.g. 'examine door'")
    print("To use an object, type use e.g. 'use door'")
    print("To see these instructions again, type 'help'\n")
    action = input()
    player_action(action)


def examine(item):
    room_item = Item(item)
    return room_item.describe()


def use(item):
    room_item = Item(item)
    return room_item.use_object()


def player_action(action):
    player_input = action.split(' ')

    if player_input[0].lower() == "help":
        initiate()
    elif player_input[0].lower() == "examine":
        examine(player_input[1].lower())
        print("")
        new_action = input()
        player_action(new_action)
    elif player_input[0].lower() == "use":
        use(player_input[1].lower())
        print("")
        new_action = input()
        player_action(new_action)
    else:
        print("Enter a valid input.\n")
        new_action = input()
        player_action(new_action)


def main():
    title()
    initiate()


main()
