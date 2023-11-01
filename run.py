# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import sys
from constants import ROOM_ITEMS, ITEM_USES, TITLE, START_TEXT, END_TEXT


class Item:
    def __init__(self, item):
        self.name = item
        self.description = ROOM_ITEMS[item]
        self.use = ITEM_USES[item]

    def describe(self):
        print(self.description)

    def use_object(self):
        print(self.use)


class Player:
    def __init__(self):
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)


def initiate(player):
    print(START_TEXT)
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
    elif item.name == "book":
        if "key" in player.inventory:
            if "page" not in player.inventory:
                player.add_to_inventory("page")
            print("You use the key to unlock the book.\n")
            print("You pick up a page that falls out as you open the book.\n")
        else:
            return player, item.use_object()
    elif item.name == "padlock":
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
    print(END_TEXT)
    player_input = input("Type restart to play again or exit to quit.\n")
    if player_input.lower() == "restart":
        main()
    elif player_input.lower() == "exit":
        sys.exit()
    else:
        end_game()


def main():
    player = Player()
    print(TITLE)
    initiate(player)


main()
