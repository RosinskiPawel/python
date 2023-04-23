import time, pathlib, random
from classes import *
from actions import *

openning()

backpack_packing_init()
print()

if task_one() > 20:
    print("You are to slowly! Try again!")
    task_one()
else:
    print(
        "\nYou feel thirsty and have a headache. Check if you have aspirin and water in your backpack. If you do, use them, otherwise you need to replenish your backpack.\n"
    )
choice = input(
    "\nWhat do you want to do now? '1': Check the backpack; '2' Change the items in my backpack or '3': Take aspirine and drink some water: \n"
)
match choice:
    case "1":
        print(f"\nHere are your items: {backpack}\n")
    case "2":
        changing_items()
    case "3":
        if "aspirin" or "water" not in backpack:
            print("You should first change you items")
            changing_items()
            print("Now you can take aspirin and drink water...")
            backpack.remove("aspirin") and ("water")
        else:
            backpack.remove("aspirin") and ("water")
            # backpack.remove("water")


# "What do you think you will need to complete the next task"
# try to quess
# right answer = 3 items: tablet, glasses and chocolate


# changing_items()

# 3 chcesz pic i boli cie noga, teraz sprawdzasz, czy masz wode/cole i apteczke

# godz = time.localtime()
# h = godz.tm_hour
# min = godz.tm_min
# print(f"It ist {h}:{min} right now!")


# def time_convert(sec):
#     mins = sec // 60
#     sec = sec % 60
#     hours = mins // 60
#     # mins = mins % 60
#     print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


# input("Press Enter to start")
# start_time = time.time()
# input("Press Enter to stop")
# end_time = time.time()
# time_lapsed = round((end_time - start_time), 2)
# time_convert(time_lapsed)
