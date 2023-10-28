# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import sys

ROOM_ITEMS = {
    "door": "A sturdy oak door locked with a solid padlock.\n",
    "padlock": "A solid steel 4-digit combination lock.\n",
    "casket": "A wooden casket with a slightly rotted lid.\n",
    "book": "An old tome that is sealed with a standard lock.\n",
    "page": "A page that fell out of the book.\n",
    "skeleton": '''It's an old skeleton. Something reflects the torchlight
from inside it's mouth.\n'''
}

ITEM_USES = {
    "door": "The door doesn't budge.\n",
    "casket": "You remove the lid and inside the casket is a skeleton.\n",
    "book": "You pick up the book. It cannot be opened without a key.\n",
    "skeleton": '''You open the mouth of a skeleton and
take a key from inside.\n''',
    "page": '''You read the text on the page:\n
    "It began with the forging of the Great Rings.
    Three were given to the Elves, immortal, wisest and fairest of all beings.
    Seven to the Dwarf lords, great miners and craftsmen
    of the mountain halls.
    And Nine, nine rings were gifted to the race of men,
    who, above all else, desire power.
    But they were, all of them, deceived, for another Ring was made.
    In the land of Mordor, in the fires of Mount Doom, the Dark Lord Sauron
    forged in secret a master Ring, to control all others.
    And into this Ring he poured his cruelty, his malice
    and his will to dominate all life.
    One Ring to rule them all."\n''',
    "padlock": None
}


class Item:
    def __init__(self, item):
        self.name = item
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

    def add_to_inventory(self, item):
        self.inventory.append(item)


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


def initiate(player):
    print("You are in a cold stone crypt, a single torch provides light.")
    print("You see a door with a padlock, a closed casket and a book.\n")
    print("To see more details, type examine e.g. 'examine door'")
    print("To use an object, type use e.g. 'use door'")
    print("To check your inventory, type inventory")
    print("To see these instructions again, type help\n")
    request_action(player)


def request_action(player):
    action = input("\n")
    validate_action(player, action)


def examine(item):
    if item in ROOM_ITEMS.keys():
        room_item = Item(item)
        return room_item.describe()
    else:
        print("There is nothing to see.\n")


def validate_use(player, item):
    if item in ITEM_USES.keys():
        room_item = Item(item)
        use(player, room_item)
    else:
        print("You cannot use that.\n")


def use(player, item):
    if item.name == "skeleton":
        if "key" not in player.inventory:
            player.add_to_inventory("key")
        return player, item.use_object()
    if item.name == "book":
        if "key" in player.inventory:
            if "page" not in player.inventory:
                player.add_to_inventory("page")
            print("You use the key to unlock the book.\n")
            print("You pick up a page that falls out as you open the book.\n")
        else:
            return player, item.use_object()
    if item.name == "padlock":
        print("The padlock has a 4 digit numerical lock.\n")
        padlock_code = input("Enter the 4 digit code:\n")
        validate_code(player, padlock_code)
    else:
        return player, item.use_object()


def validate_code(player, code):
    try:
        int(code)
        if len(code) == 4:
            use_padlock(player, code)
        else:
            new_code = input("Please enter a 4 digit number:\n")
            validate_code(player, new_code)
    except ValueError:
        new_code = input("Please enter a 4 digit number:\n")
        validate_code(player, new_code)


def use_padlock(player, code):
    if int(code) == 3791:
        end_game()
    else:
        print('''You enter the numbers into the padlock,\n
        but it does not budge.\n''')
        initiate(player)


def check_inventory(player):
    if len(player.inventory) == 0:
        print("You have nothing in your inventory.\n")
    else:
        print("You have the following items in your inventory:\n")
        for item in player.inventory:
            print(item)


def validate_action(player, action):
    player_input = action.split(' ')

    if player_input[0].lower() == "help":
        initiate(player)
    elif player_input[0].lower() == "inventory":
        check_inventory(player)
        request_action(player)
    elif player_input[0].lower() == "examine":
        examine(player_input[1].lower())
        request_action(player)
    elif player_input[0].lower() == "use":
        validate_use(player, player_input[1].lower())
        request_action(player)
    else:
        print("Enter a valid input.\n")
        request_action(player)


def end_game():
    print("As the numbers click into place, the padlock opens.")
    print("You push the door and it swings open.")
    print("You have escaped!\n")
    print("Thank you for playing!\n")
    player_input = input("Type restart to play again or exit to quit.\n")
    if player_input.lower() == "restart":
        main()
    elif player_input.lower() == "exit":
        sys.exit()
    else:
        end_game()


def main():
    player = Player()
    title()
    initiate(player)


main()
