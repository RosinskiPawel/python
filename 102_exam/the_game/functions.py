import time
from classes import *
from datetime import datetime

backpack = []
pool_items = (
    "cat",
    "can opener",
    "aspirin",
    "chocolate",
    "water",
    "tablet",
    "glasses",
    "flashlight",
    "calculator",
)

words = (
    "day",
    "night",
    "you",
    "me",
    "we",
    "are",
    "all",
    "happy",
    "I",
    "sun",
)


def openning():
    f = open("the_game\\text\\intro.txt")
    print(f.read())
    player = Player(
        name=input("\nPlease input your name... \n"),
        birth_date=input(
            "\n...and date of birth in format YYYYMMDD. This information will be needed in the later stage of the game: \n"
        ),
    )
    if input(f"\n{player.name}, press Enter to start \n") == "":
        print("Let's start!")
    return player.birth_date


def task_one():
    task1 = open("the_game\\text\\task1.txt")
    print(task1.read())
    choosen_excercise = Gym(
        input("\nWhat excercise do you choose? \nSquats or push_ups\n").lower()
    )

    input("\nPress Enter to start\n")
    start_time = time.time()
    input("Press Enter to stop\n")
    end_time = time.time()
    time_total = round((end_time - start_time), 2)
    print(
        f"\nThis is your time: {time_total} seconds. You have burned ca. {Gym.burnedCalories(choosen_excercise.calories_per_min, time_total)} calories.\n"
    )
    return time_total


def backpack_packing_init():
    print(
        "\nChoose three items from the list below that you think will be useful for the this task.\n"
    )
    for i in pool_items:
        print(f"{pool_items.index(i)+1}. {i}")
    print()
    for i in range(3):
        item = input(f"\nAdd {i+1}. item: ")
        while item not in pool_items:
            print("\nWrong item")
            item = input(f"\nAdd {i+1}. item: ")
        Player.backpack.append(item)
    print(f"\nYou have chosen {Player.backpack}.\n")


def changing_items():
    print(f"\nHere are your items: {Player.backpack}.")
    num_of_items_del = int(input("\nHow many items do you want to delete? "))

    for i in range(num_of_items_del):
        item_to_delete = input(f"\nPlease choose the {i+1}.item to delete: ")
        Player.backpack.remove(item_to_delete)

    for i in range(num_of_items_del):
        item_to_add = input(f"\nPlease choose the {i+1}.item to add: ")
        while item_to_add not in pool_items:
            print("\nWrong item")
            item_to_add = input(f"\nPlease choose the {i+1}.item to add: ")
        Player.backpack.append(item_to_add)
    print(f"\nHere are your new items: {Player.backpack}.")


def fill_up_backpack():
    max_numb_items = 3
    numb_items = len(Player.backpack)
    numb_to_add = max_numb_items - numb_items
    print(f"You can add {numb_to_add} items.")
    for i in range(numb_to_add):
        item = input(f"\nAdd {i+1}. item: ")
        while item not in pool_items:
            print("\nWrong item")
            item = input(f"\nAdd {i+1}. item: ")
        Player.backpack.append(item)
    print(f"\nThis is your backpack: {Player.backpack}.")


def using_items():
    Player.show_backpack(Player)
    num_of_items_use = int(input("\nHow many items do you want to use? "))
    for i in range(num_of_items_use):
        item_to_use = input(f"\nPlease choose the {i+1}.item to use: ")
        Player.backpack.remove(item_to_use)


def options_to_choose():
    while True:
        option = input(
            "Choose the option:\n 'a' = checking the backpack\n 's' = changing items\n 'd' = using items\n 'f' = filling up the backpack\n"
        )
        if option == "a":
            Player.show_backpack(Player)
        elif option == "s":
            changing_items()
        elif option == "d":
            using_items()
        elif option == "f":
            fill_up_backpack()
        question = input("Wanna see the options again? (y/n):  ").lower()
        if question == "y":
            True
        else:
            break


def task_two():
    temp_list = []
    print(f"\nHere is the list of words. Please use minimum five of them: {words}")
    while True:
        note = input("\nPlease write a few sentences:\n ")
        for i in words:
            if i in note.split():
                temp_list.append(i)
        if len(temp_list) < 5:
            print(
                "You haven't used at least five words from the list. Please try again!"
            )
            True
        else:
            print("Well done. The task is completed")
            break


def safe_code():
    now = datetime.now()
    date_now = "".join((str(now).split())[0].split("-"))
    return date_now - Player.self.birth_date


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


# def print_to_file():

# def read_from_file():
