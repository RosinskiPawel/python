import time
from datetime import datetime
from classes import *
from functions import *

# def time_convert(sec):
#     mins = sec // 60
#     sec = sec % 60
#     hours = mins // 60
#     mins = mins % 60
#     print("Your time = {0}:{1}:{2}".format(int(hours), int(mins), sec))

# def my_tconv(msec):


# input("Press Enter to start")
# start_time = time.time()
# input("Press Enter to stop")
# end_time = time.time()
# time_total = end_time - start_time
# time_lapsed = round((end_time - start_time), 0)
# # time_convert(time_lapsed)
# print(time_lapsed)


# class Gym:
#     calories_per_min = 0

#     def __init__(self, name):
#         self.name = name
#         if self.name == "squats":
#             self.calories_per_min = 7
#         elif self.name == "push_ups":
#             self.calories_per_min = 12

#         # self.calories_per_min = calories_per_min

#     def burnedCalories(calories_per_min, exercise_time):
#         return float(calories_per_min * exercise_time)


# words = "day", "night", "you", "me", "we", "are", "all", "happy"


# def write_note():
#     temp_list = []
#     print(f"Here is the list of words. Pleas use minimum five of them: {words}")
#     while True:
#         note = input("Please write a few sentences: ")
#         for i in words:
#             if i in note.split():
#                 temp_list.append(i)
#         if len(temp_list) < 5:
#             print("Try again!")
#             True
#         else:
#             print("Well done. The task is completed")
#             break


# player = Player(
#     name=input("\nPlease input your name... \n"),
#     birth_date=input(
#         "\n...and date of birth in format RRRRMMDD. This information will be needed in the later stage of the game: \n"
#     ),
# )

# date_now = datetime.now()
# print(date_now)
# print("".join((str(date_now).split())[0].split("-")))

# while True:
#     if task_one() > 20:
#         print("You are to slowly! Try again!")
#         True
#     else:
#         print(
#             "\nYou feel thirsty and have a headache. Check if you have aspirin and water in your backpack. If you do, use them, otherwise you need to replenish your backpack.\n"
#         )
#         break

# print(open("the_game\\text\\task3.txt").read())

player = ""


def openning():
    f = open("the_game\\text\\intro.txt")
    print(f.read())
    player = Player(
        name=input("\nPlease input your name... \n"),
        birth_date=input(
            "\n...and date of birth in format YYYYMMDD. This information will be needed in the later stage of the game: \n"
        ),
    )
    print(player.name)
    print(player.birth_date)


def safe_code():
    now = datetime.now()
    date_now = "".join((str(now).split())[0].split("-"))
    return int(date_now - Player.birth_date)


def task_three():
    while True:
        subtraction_result = input("Please enter your result of substraction: ")
        safe_code()
        if safe_code != subtraction_result:
            print("Wrong value, please try again!")
            return True
        else:
            print("Excellent. You did it!")
            break


openning()
task_three()
