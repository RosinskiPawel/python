import time, pathlib, random
from classes import *
from functions import *
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
        print(open("the_game\\text\\task1_after.txt").read())
        break
while True:
    if input("Press 'o' to see options to choose\n") != "o":
        True
    else:
        options_to_choose()
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

print(open("the_game\\text\\task2.txt").read())
options_to_choose()
task_two()
print(open("the_game\\text\\task3.txt").read())
options_to_choose()
task_three()
