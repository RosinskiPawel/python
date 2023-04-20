# from classes import Items, Table, Knife
from classes import *
import time
from actions import *

# import actions


# f = open("the_game\\text\\intro.txt")
# print(f.read())

if openning() == True:
    player_1 = Player(input("What's your name? "))

    print(f"Welcome, {player_1.name}")
else:
    print("Bye!")


# coin = Items("coin", "under the table")
# print(f"I have found the coin {coin.location}")

# longKnife = Knife("loooongy", "on the table", 10)

# print(f"I have a {longKnife.length}-inch knife!")
# table = Table("oval", "room_1")
# print(f"The table is in {table.location}")

# godz = time.localtime()
# h = godz.tm_hour
# min = godz.tm_min
# print(f"It ist {h}:{min} right now!")


# take("ring")

# print(pocket[0])

import time


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    # mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


input("Press Enter to start")
start_time = time.time()
input("Press Enter to stop")
end_time = time.time()
time_lapsed = round((end_time - start_time), 2)
time_convert(time_lapsed)
