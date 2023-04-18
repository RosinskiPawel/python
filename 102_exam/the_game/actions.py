def openning():
    f = open("the_game\\text\\intro.txt")
    print(f.read())
    question_1 = input("Do you want to read the letter? Y/N ").lower()

    if question_1 == "y":
        letter = open("the_game\\text\\letter.txt")
        print(letter.read())
    else:
        print("No problem!")
    return


def move_forward(steps):
    print(f"Move forward {steps} steps")


def move_back(steps):
    print(f"Move back {steps} steps")


pocket = []


def take(string):
    pocket_numb = 4
    if len(pocket) < pocket_numb:
        pocket.append(string)
        print(f"You have taken the {string}.")
    else:
        print(f"You can't take it. Your pockets are full.")
    return


def empty_pockets():
    item = input("what do you want to remove from your pockets? ")
    return pocket.remove(item)
