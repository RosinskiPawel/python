#----------8.3---------------
#1
##word_to_comp = input("Enter a word ")
##number = 5
##if len(word_to_comp) > 5:
##    print("Your input is grteater then 5 char. long.")
##elif len(word_to_comp) < 5:
##    print("Your input is less then 5 char. long.")
##else: print("Your input is 5 char. long.")
##    
###2
##import random
##rand_numb = random.randint(1, 11)
##guessed_numb = input("Guess the number ")
##if guessed_numb == rand_numb:
##    print("You win!")
##else: print("You loose!")

    
#====8.4 Challenge=====
pos_int = int(input("enter a positive integer "))
for i in range(1, pos_int+1):
    
    if pos_int % i == 0:
        print(f"{i} is a factor of {pos_int}")    
    
    
