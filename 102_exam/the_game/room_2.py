def take2(item):
    pocket.append(item)
    print(f"You have taken the {item}.")


pocket = []

take2("coin")
print(pocket[0])


def take3(string):
    pocket_numb = 4
    if len(pocket) < pocket_numb:
        pocket.append(string)
        print(f"You have taken the {string}.")
    else:
        print(f"You can't take it. Your pockets are full.")

    return


take3("1")
take3("2")
take3("3")
take3("4")
take3("5")


def empty_pockets():
    item = input("what do you want to remove from your pockets? ")
    return pocket.remove(item)


empty_pockets()
print(pocket)
