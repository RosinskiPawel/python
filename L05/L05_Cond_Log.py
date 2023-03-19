#----------8.3---------------
#1
word_to_comp = input("Enter a word ")
number = 5
if len(word_to_comp) > 5:
    print("Your input is grteater then 5 char. long.")
elif len(word_to_comp) < 5:
    print("Your input is less then 5 char. long.")
else: print("Your input is 5 char. long.")
    
#2
import random
rand_numb = random.randint(1, 11)
guessed_numb = input("Guess the number ")
if guessed_numb == rand_numb:
    print("You win!")
else: print("You loose!")

    
#====8.4 Challenge=====
pos_int = int(input("enter a positive integer "))
for i in range(1, pos_int+1):
    if pos_int % i == 0:
        print(f"{i} is a factor of {pos_int}")    
    


#+-----8.5-------
#1
  
x = ' '
while x != 'q':
    x = input("enter char. ")
    if x.lower() == 'q':
        print("Entered 'Q' or 'q'. Break.")
        break
    print(x)


    
        
#2
for i in range (1,51):
    if i%3==0:
        continue
    print(i)



#-----8.6----
#1
for i in range(4):
    try:
        numb = int(input("Enter a number "))
    except ValueError:
        print("Not an int. Try again!")
    if i == 2:
        print("Your last chance!")
print(numb)
    
    
while True:
    try:
        numb = int(input("Enter a number: "))
        print(f"Excellent!!! You have entered a number: {numb}.")
        break
    except ValueError:
        print("Please enter a number!")
        
#2

##text = input("Enter a word: ")
##for i in range(10):
##    try:
##        index = int(input("enter an index: "))
##        print(f"{text[index]}")
##        break
##    except IndexError:
##        print("index too large")
##    except ValueError:
##        print("Enter a number")
        

text = input("Enter a word: ")
while True:
    try:
        index = int(input("enter an index: "))
        print(f"A character with index ({index}) is '{text[index]}'.")
        break
    except IndexError:
        print("The index is too big!")
    except ValueError:
        print("Enter a number!")

while True:
    try:
        text1 = int(input('input a number '))
        print(text1)
        break
    except ValueError:
        print("Ups! Try again!")
        
            
##x=1
##while x <6:
##    print('o'*x)
##    x=x+1
##
##
##x=1
##while x <10:
##    print(x*str(x ))
##    x=x+1
##        
##
##for i in range(10):
##    print(i*str(i))
##

        
#--------8.7-------
#1
import random

def roll():
    x = random.randint(1,6)
    return x

#2
import random
total = 0
for i in range(10000):
    x = random.randint(1,6)
    total = total+x
print(round((total/10000), 2))

#+=====8.8 Challenge======

import random
##box = ['heads', 'tails']
total_heads = 0
total_tails = 0
for i in range(10000):
    x = random.randint(0, 1)
    if x == 0:
        total_heads = total_heads + 1
    else:
        total_tails = total_tails + 1
print(f"Heads: {total_heads}. Tails: {total_tails}")

    
import random
box = ['heads', 'tails']
total_heads = 0
total_tails = 0
for i in range(10000):
    x = random.choices(box, k=2)
    if x == ['heads', 'heads']:
        total_heads = total_heads + 1
    elif x == ['tails', 'tails']:
        total_tails = total_tails + 1
print(f"Heads: {total_heads}. Tails: {total_tails}")

   
#+=====8.9 Challenge======


import random

def prob_of_winning(prob):
    if random.random() < prob:
        return 0
    else:
        return 1

candA = 0
candB = 0
winnerA = 0
winnerB = 0

for n in range(10_000):
    if prob_of_winning(.87) == 0:
        candA = candA + 1
    if prob_of_winning(.65) == 0:
        candA = candA + 1
    if prob_of_winning(.17) == 0:
        candA = candA + 1
    else: candB = candB + 1
    if candA>candB:
            winnerA = winnerA+1
    else: winnerB = winnerB+1
    
print(f"{winnerA*100/10000}%")
        
        

        
        





