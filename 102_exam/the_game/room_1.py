import time, pathlib, random
from classes import *
from actions import *
from datetime import datetime


# if task_one() > 20:
#     print("You are to slowly! Try again!")
#     task_one()
# else:
#     print(
#         "\nYou feel thirsty and have a headache. Check if you have aspirin and water in your backpack. If you do, use them, otherwise you need to replenish your backpack.\n"
#     )


openning()
backpack_packing_init()
while True:
    min_time = 20
    if task_one() > min_time:
        print("You are to slowly! Try again!\n")
        True
    else:
        print(
            "\nYou feel thirsty and have a headache. Check if you have aspirin and water in your backpack. If you do, use them, otherwise you need to replenish your backpack.\n"
        )
        break
while True:
    if input("Press 'o' to see options to choose\n") != "o":
        True
    else:
        help()
        break


# choice = input(
#     "\nWhat do you want to do now? '1' Change the items in my backpack or '2': Take aspirin and drink some water: \n"
# )
# match choice:
#     case "1":
#         changing_items()
#         using_items()
#     case "2":
#         if ("aspirin" or "water") not in Player.backpack:
#             print("You should first change you items")
#             changing_items()
#             print("Now you can take aspirin and drink water...")
#             using_items()
#         else:
#             using_items()

if input(f"\nIf you are ready for the 2. task, press Enter \n") == "":
    print("Let's continue the game!")

taks_two_text = open("the_game\\text\\task2.txt")
print(taks_two_text.read())

help()

write_note()

# You have completed all the tasks, the last and most important one is ahead of you. You must open the safe. To do this, you need can opener, calculator and the cat. Check if you have them in your backpack, if not, you know what to do....
