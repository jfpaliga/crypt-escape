from constants import ROOM_ITEMS, ITEM_USES
from run import Item


def validate_action(player, action):
    player_input = action.split(' ')
    choice = player_input[0].lower()
    if len(player_input) == 2:
        item = player_input[1].lower()

    if choice == "help":
        player.start_game()
    elif choice == "inventory":
        player.check_inventory()
        player.get_action()
    elif choice == "examine":
        Item.examine(item)
        player.get_action()
    elif choice == "use":
        validate_use(player, item)
        player.get_action()
    else:
        print("Enter a valid input.\n")
        player.get_action()


def validate_use(player, item):
    if item in ITEM_USES.keys():
        room_item = Item(item, ROOM_ITEMS[item], ITEM_USES[item])
        player.use(room_item)
    else:
        print("You cannot use that.\n")


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
        player.end_game()
    else:
        print('''You enter the numbers into the padlock,\n
        but it does not budge.\n''')
        player.start_game()
        