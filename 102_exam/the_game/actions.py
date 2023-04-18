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
