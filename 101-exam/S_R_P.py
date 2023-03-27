import random
list_of_options = ['rock', 'paper', 'scissors']
invitation = input("If you want to play, please type 'y' for yes or 'n' for no  ").lower()
while invitation == 'y':
    player = input("Please choose one option: scissors, rock or papper: ").lower()
    comp = list_of_options[random.randint(0, len(list_of_options)-1)]
    if player == comp:
        print("It's a draw")
    elif ((comp == 'scissors') and (player == 'rock')) or ((comp == 'rock') and (player == 'paper')) or ((comp == 'paper') and (player == 'scissors')):
        print(f" I have chosen '{comp}', you '{player}'. So you win! Congratulations!!!!")
    else: print(f" I have chosen '{comp}', you '{player}'. I win. Don't worry!")
    invitation = input("Wanna play again? ").lower()
print("Thank you! See you latter!")