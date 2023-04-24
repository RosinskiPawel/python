import time
from classes import *

backpack = []
pool_items = (
    "cat",
    "can opener",
    "aspirin",
    "chocolate bar",
    "water",
    "tablet",
    "glasses",
    "flashlight",
    "home map",
)


def openning():
    f = open("the_game\\text\\intro.txt")
    print(f.read())
    player = Player(name=input("\nWhat's your name? \n"))
    question_1 = input(
        f"\n{player.name}, are you ready for the first task? Y/N \n"
    ).lower()
    if question_1 == "y":
        print("Let's start!")
    else:
        print("Bye!")
        return


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
        f"\nThis is your time: {time_total} seconds. You have burned ca. {Gym.burnedCalories(choosen_excercise.calories_per_min, time_total)} calories"
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
    print(f"\nYou have chosen {Player.backpack}.")


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


def using_items():
    num_of_items_use = int(input("\nHow many items do you want to use? "))
    for i in range(num_of_items_use):
        item_to_use = input(f"\nPlease choose the {i+1}.item to use: ")
        Player.backpack.remove(item_to_use)


def help():
    option = input(
        "Choose the option:\n 'a' = checking the backpack\n 's' = changing items\n 'd' = using items\n"
    )
    if option == "a":
        Player.show_backpack(Player)
    elif option == "s":
        changing_items()
    elif option == "d":
        using_items()


# def print_to_file():

# def read_from_file():
