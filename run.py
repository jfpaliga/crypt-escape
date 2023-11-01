import sys
from constants import ROOM_ITEMS, ITEM_USES, TITLE, START_TEXT, END_TEXT
from utils import validate_action, validate_use, validate_code, use_padlock


class Item:
    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use

    def describe(self):
        print(self.description)

    def use_object(self):
        print(self.use)

    @staticmethod
    def examine(item):
        if item in ROOM_ITEMS.keys():
            room_item = Item(item, ROOM_ITEMS[item], ITEM_USES[item])
            return room_item.describe()
        else:
            print("There is nothing to see.\n")


class Player:
    def __init__(self):
        self.inventory = []

    def start_game(self):
        print(START_TEXT)
        self.get_action()

    def end_game(self):
        print(END_TEXT)
        while True:
            _input = input("Type restart to play again or exit to quit.\n")
            if _input.lower() == "restart":
                self.inventory = []
                print(TITLE)
                self.start_game()
            elif _input.lower() == "exit":
                sys.exit()

    def get_action(self):
        action = input("\n")
        validate_action(self, action)

    def check_inventory(self):
        if len(self.inventory) == 0:
            print("You have nothing in your inventory.\n")
        else:
            print("You have the following items in your inventory:\n")
            for item in self.inventory:
                print(item)

    def use(self, item):
        if item.name == "skeleton":
            if "key" not in self.inventory:
                self.add_to_inventory("key")
            return item.use_object()
        elif item.name == "book":
            if "key" in self.inventory:
                if "page" not in self.inventory:
                    self.add_to_inventory("page")
                print("You use the key to unlock the book.\n")
                print("You pick up a page that falls out as you open it.\n")
            else:
                return item.use_object()
        elif item.name == "padlock":
            print("The padlock has a 4 digit numerical lock.\n")
            padlock_code = input("Enter the 4 digit code:\n")
            validate_code(self, padlock_code)
        else:
            return item.use_object()

    def add_to_inventory(self, item):
        self.inventory.append(item)


if __name__ == "__main__":
    print(TITLE)
    player = Player()
    player.start_game()
