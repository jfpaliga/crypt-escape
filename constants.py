ROOM_ITEMS = {
    "door": "A sturdy oak door locked with a solid padlock.",
    "padlock": "A solid steel 4-digit combination lock.",
    "casket": "A wooden casket with a slightly rotted lid.",
    "book": "An old tome that is sealed with a standard lock.",
    "page": "A page that fell out of the book.",
    "skeleton": '''It's an old skeleton. Something reflects the torchlight
from inside it's mouth.'''
}

ITEM_USES = {
    "door": "The door doesn't budge.",
    "casket": "You remove the lid and inside the casket is a skeleton.",
    "book": "You pick up the book. It cannot be opened without a key.",
    "skeleton": '''You open the mouth of the skeleton and
take a key from inside.''',
    "page": '''You read the text on the page:
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
    One Ring to rule them all."''',
    "padlock": None
}

TITLE = r'''
 _____                  _     _____                         
/  __ \                | |   |  ___|                        
| /  \/_ __ _   _ _ __ | |_  | |__ ___  ___ __ _ _ __   ___ 
| |   | '__| | | | '_ \| __| |  __/ __|/ __/ _` | '_ \ / _ \
| \__/\ |  | |_| | |_) | |_  | |__\__ \ (_| (_| | |_) |  __/
 \____/_|   \__, | .__/ \__| \____/___/\___\__,_| .__/ \___|
             __/ | |                            | |         
            |___/|_|                            |_|         
            
Welcome to Crypt Escape!

        '''

START_TEXT = r'''
You are in a cold stone crypt, a single torch provides light.
You see a door with a padlock, a closed casket and a book.
To see more details, type examine e.g. 'examine door'
To use an object, type use e.g. 'use door'
To check your inventory, type inventory
To see these instructions again, type help
            '''

END_TEXT = r'''
As the numbers click into place, the padlock opens.
You push the door and it swings open.
You have escaped!
Thank you for playing!

            '''
