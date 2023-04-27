import time, pathlib, random
from classes import *
from functions import *
from datetime import datetime

player = Player(
    name=input("\nPlease enter your name... \n"),
    birth_date=input(
        "\n...and date of birth in format YYYYMMDD. This information will be needed in the later stage of the game: \n"
    ),
)
print(open("the_game\\text\\intro.txt").read())
if input(f"\n{player.name}, press Enter to start \n") == "":
    print("Let's start!")

backpack_packing_init()
task_one_result()

while True:
    if ("aspirin" or "water") in Player.backpack:
        print("Take aspirin and drink water to go ahead.")
        options_to_choose()
        True
    else:
        break

if (
    input(
        f"\nYou have completed the task one. If you are ready for the 2. task, press Enter \n"
    )
    == ""
):
    print("Let's continue the game!")

print(open("the_game\\text\\task2.txt").read())
options_to_choose()

while True:
    if ("tablet" and "glasses" and "chocolate") not in Player.backpack:
        print("For this task you need: tablet, glasses and chocolate.")
        options_to_choose()
        True
    else:
        break

task_two()
print(open("the_game\\text\\task3.txt").read())
options_to_choose()


task_three()
