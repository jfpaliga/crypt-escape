# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

ROOM_OBJECTS = {
    "door": "A sturdy oak door locked with a solid padlock",
    "padlock": "A solid steel 4-digit combination lock",
    "casket": "A wooden casket with a slightly rotted lid",
    "book": "An old tome that is sealed with a standard lock"
}


class Object:
    def __init__(self, description):
        self.description = description

    def describe(self):
        print(self.description)


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
    room_item = Object(ROOM_OBJECTS[item])
    return room_item.describe()


def player_action(action):
    player_input = action.split(' ')

    if player_input[0].lower() == "help":
        initiate()
    elif player_input[0].lower() == "examine":
        examine(player_input[1].lower())
    else:
        print("Enter a valid input.")
        new_action = input()
        player_action(new_action)


def main():
    title()
    initiate()


main()
