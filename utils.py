from constants import ROOM_ITEMS, ITEM_USES


def validate_action(player, action):
    """
    Take player input and split it into a list. Check the list
    for keywords and execute an appropriate Player class method.

    After calling the class method, call the Player.get_action()
    method to get another input from the player to continue the
    game.

    Returns
    -------
    None
    """

    from run import Item
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
    """
    Take a passed string and check if it exists as a key in the
    ITEM_USES dictionary.

    If it does, instantiate item as an Item object and call the
    Player.use() class method using the new Item object.

    Otherwise, print a statement to inform the player they cannot
    use that item.

    Returns
    -------
    None
    """

    from run import Item
    if item in ITEM_USES.keys():
        room_item = Item(item, ROOM_ITEMS[item], ITEM_USES[item])
        player.use(room_item)
    else:
        print("You cannot use that.\n")


def validate_code(player, code):
    """
    Pass player input through a try/except loop to validate that the
    input is an integer. Within the try loop, check that the integer
    is 4 digits long.

    If both cases pass, the use_padlock() function is called.

    Otherwise, ask for a valid input and pass the new input
    back into this function.

    Returns
    -------
    None
    """

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
    """
    Check whether the passed code matches with an integer. If so,
    call the Player.end_game() class method.

    Otherwise, print a statement to inform the player their
    input was incorrect and call the Player.get_action() class method.

    Returns
    -------
    None
    """

    if int(code) == 3791:
        player.end_game()
    else:
        print('''You enter the numbers into the padlock,\n
        but it does not budge.\n''')
        player.get_action()
