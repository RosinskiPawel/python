import random

step = "|\n"
f = "______"
g = "|    |"
h = "|    O"
i = "|   ~|~"
j = "|   | |"

step1 = 2 * step
step2 = 2 * step1
step3 = f"{f}\n{g}\n{step2}"
step4 = f"{f}\n{g}\n{h}\n{3*step}"
step5 = f"{f}\n{g}\n{h}\n{i}\n{2*step}"
step6 = f"{f}\n{g}\n{h}\n{i}\n{j}\n{step}"
steps = [step1, step2, step3, step4, step5, step6]

pool_names = [
    "Agata",
    "Hania",
    "Janek",
    "Konstanty",
    "Hermenegilda",
    "Maurycy",
    "Krystian",
    "Maria",
]
pool_countries = [
    "Polska",
    "Grecja",
    "Niemcy",
    "Liban",
    "Izrael",
    "Kanada",
    "Honduras",
    "Chorwacja",
]
pool_cities = (
    "Monachium",
    "Berlin",
    "Sopot",
    "Zakopane",
    "Praga",
    "Jerozolima",
    "Londyn",
    "Jerozolima",
)


def choosing_cat():
    category = input("Choose the category: 1 - Names, 2 - Countries, 3 - Cities  \n")
    if category == "1":
        word_to_guess = random.choice(pool_names)
    elif category == "2":
        word_to_guess = random.choice(pool_countries)
    elif category == "3":
        word_to_guess = random.choice(pool_cities)
    return word_to_guess


def hidden():
    letter = 0
    for i in range(len(word_to_guess)):
        hidden_letters.append("_ ")
        letter = letter + 1
    print("".join(hidden_letters))
    print(f"Guess a word with {letter} letters.")


while True:
    word_to_guess = choosing_cat()
    hidden_letters = []
    z = 0
    hidden()

    while True:
        guess = input("Input a letter:   ")
        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    hidden_letters[i] = guess + " "
            print("".join(hidden_letters))
            if "_ " not in hidden_letters:
                print("Winner")
                break
        else:
            print(steps[z])
            z = z + 1
            if z == len(steps):
                print(f"I'm sorry, you loose. The word to guess was {word_to_guess}")
                break
    if input("Do you want to play again (y/n)?\n") == "y":
        True
    else:
        break
