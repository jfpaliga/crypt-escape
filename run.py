import sys
from constants import ROOM_ITEMS, ITEM_USES, TITLE, START_TEXT, END_TEXT
from utils import validate_action, validate_use, validate_code, use_padlock


class Item:
    """
    A class to represent an item in the game.

    Attributes
    ----------
    name : str
        The name of the item
    description : str
        The description of the item
    use : str
        The outcome of using the item

    Methods
    -------
    describe():
        Print a description of the item.
    use_item():
        Print the outcome of using the item.
    examine(item):
        Return the Item.describe() function if a passed
        item is valid.
    """

    def __init__(self, name, description, use):
        """
        Construct the necessary parameters for the Item object.

        Parameters
        ----------
            name : str
                The name of the item.
            description : str
                The description of the item.
            use : str
                The outcome of using the item.
        """

        self.name = name
        self.description = description
        self.use = use

    def describe(self):
        """Print a description of the item."""

        print(self.description)

    def use_item(self):
        """Print the outcome of using the item."""

        print(self.use)

    @staticmethod
    def examine(item):
        """
        Determine whether a passed item is valid (ie if it is a key in the
        ROOM_ITEMS dictionary), and then return the Item.describe() method.

        Returns
        -------
        Item.describe()
        """

        if item in ROOM_ITEMS.keys():
            room_item = Item(item, ROOM_ITEMS[item], ITEM_USES[item])
            return room_item.describe()
        else:
            print("There is nothing to see.\n")


class Player:
    """
    A class to represent the player of the game.

    Attributes
    ----------
    None

    Methods
    -------
    start_game():
        Print START_TEXT and player instructions, then call the
        Player.get_action() method.
    end_game():
        Print END_TEXT to indicate completion of the game.
        Get player input to either restart the game or exit.
    get_action():
        Get player input and pass to the validate_action() function
        in utils.py.
    check_inventory():
        Check the length of the Player.inventory list and print an
        appropriate statement.
    use(item):
        Return the Item.use_item() method unless the passed item is
        an exception.
    add_to_inventory(item):
        Append the name of the passed item to the players inventory list.
    """

    def __init__(self):
        """
        Construct the necessary parameters for the Player object.

        Parameters
        ----------
            inventory : list
                A list of items in the players inventory.
        """

        self.inventory = []

    def start_game(self):
        """
        Print START_TEXT and player instructions, then call the
        Player.get_action() method.

        Returns
        -------
        None
        """

        print(START_TEXT)
        self.get_action()

    def end_game(self):
        """
        Print END_TEXT to indicate completion of the game.
        Get player input to either restart the game or exit.

        Returns
        -------
        None
        """

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
        """
        Get player input and pass to the validate_action() function
        in utils.py.

        Returns
        -------
        None
        """

        action = input("\n")
        validate_action(self, action)

    def check_inventory(self):
        """
        Check the length of the Player.inventory list and print an
        appropriate statement.

        If the length of the Player.inventory list = 0 print a statement
        to indicate the inventory is empty.

        Otherwise, print the Player.inventory list.

        Returns
        -------
        None
        """

        if len(self.inventory) == 0:
            print("You have nothing in your inventory.\n")
        else:
            print("You have the following items in your inventory:\n")
            for item in self.inventory:
                print(item)

    def use(self, item):
        """
        Return the Item.use_item() method unless the passed item is
        an exception.

        In the case of the 'skeleton' and 'book' items, add an item to the 
        Player.inventory list and print additional text.

        In the case of the 'padlock', get player input and pass to the
        validate_code() function in utils.py.

        Returns
        -------
        Item.use_item()
        """

        if item.name == "skeleton":
            if "key" not in self.inventory:
                self.add_to_inventory("key")
            return item.use_item()
        elif item.name == "book":
            if "key" in self.inventory:
                if "page" not in self.inventory:
                    self.add_to_inventory("page")
                print("You use the key to unlock the book.\n")
                print("You pick up a page that falls out as you open it.\n")
            else:
                return item.use_item()
        elif item.name == "padlock":
            print("The padlock has a 4 digit numerical lock.\n")
            padlock_code = input("Enter the 4 digit code:\n")
            validate_code(self, padlock_code)
        else:
            return item.use_item()

    def add_to_inventory(self, item):
        """Append the name of the passed item to the players inventory list."""

        self.inventory.append(item)


if __name__ == "__main__":
    print(TITLE)
    player = Player()
    player.start_game()
