# from classes import Items, Table, Knife
from classes import *
import time
from actions import pocket
import actions


f = open("the_game\\text\\intro.txt")
print(f.read())


coin = Items("coin", "under the table")
print(f"I have found the coin {coin.location}")

longKnife = Knife("loooongy", "on the table", 10)

print(f"I have a {longKnife.length}-inch knife!")
table = Table("oval", "room_1")
print(f"The table is in {table.location}")

godz = time.localtime()
h = godz.tm_hour
min = godz.tm_min
print(f"It ist {h}:{min} right now!")


actions.take("ring")

print(pocket[0])
