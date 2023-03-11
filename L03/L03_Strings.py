#-----4.1--------

#1
newText = 'This is so called "new land" for the last people on earth.'
print(newText)

#2
newText = "This is my whife's best chicken ever."
print(newText)

#3
newText = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(newText)

#4
newText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod\
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo \
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse \
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat \
non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(newText)


#--------4.2------

#1
newText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod\
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo \
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse \
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat \
non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
newTextLength = len(newText)
print(newTextLength)
#OR
print(len(newText))

#2
firstStr = "avo"
secondStr = "cado"
completedText = firstStr + secondStr
print(completedText)
#OR
print(firstStr+secondStr)

#3
firstStr = "Avo"
secondStr = "Cado"
print(firstStr+" " + secondStr)

#4
str_n = 'bazinga'
print(str_n[2:])


#-------4.3----------
#1
first = "Animals"
second = "Badger"
third = "Honey Bee"
fourth = "Honey Badger"
print(first.lower())
print(second.lower())
print(third.lower())
print(fourth.lower())

#2
first = "Animals"
second = "Badger"
third = "Honey Bee"
fourth = "Honey Badger"
print(first.upper())
print(second.upper())
print(third.upper())
print(fourth.upper())

#3
string1 = "     Filet Mignon"
string2 = "Brisket     "
string3 = "     Cheesburger     "
print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

#4
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "    bEAR"
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

#5
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "    bEAR"
print(string1.lower().startswith("be"))
print(string2.startswith("be"))
print(string3.lower().startswith("be"))
print(string4.lower().lstrip().startswith("be"))

#----------4.4-------
#1
question = ("What's your name?")
answer = input(question)
print("Hello,", answer)

#2
task = ("Please, type few words")
words = input(task)
print("You have typed: ", words.upper())

#3
task = ("Please, type a short text")
words = input(task)
print("characters: ", len(words))

#----CHALLENGE 4.5------
input_data = ("Tell me your password")
new_pass = input(input_data)
first_letter_of_pass = new_pass[0].upper()
print("The first letter you entered was:", first_letter_of_pass)


#------4.6-------

#1
text = '2'
multi = int(text)*2
print(multi)
#2
text = '2.3'
multi = float(text)*2
print(multi)

#3

text = '123'
number = 321
print(text+str(number))

#4
first_command = ("Input first number: ")
first_numb = input(first_command)
second_command = ("Input second numer: ")
second_numb = input(second_command)
multi = float(first_numb)*float(second_numb)
print("The product of "+first_numb+" and "+second_numb+" is "+str(multi))
      

#-----------4.7------
#1
weight = 0.2
animal = "newt"
print(str(weight) +" kg is the weight of the "+animal+".")
#2
weight = 0.2
animal = "newt"
print("{}kg is the weight of the {}".format(weight, animal))
#3
weight = 0.2
animal = "newt"
print(f"{weight} kg is the weight of the {animal}.")

#------4.8-----

#1
text2 = 'AAA'
text2.find('a')

#2
text3 = "Somebody said something to Samantha"
text3.replace('s', 'x')

#3

print("Somebody said something to Samantha")
main_text = "Somebody said something to Samantha"
text3 = "What letter should I find?"
letter_to_find = input(text3)
print(f"The letter '{letter_to_find}' has index {main_text.find(letter_to_find)}.")

#--------4.9--------
text5 = ("Enter some text: ")
text_to_modify = input(text5)
new_text = text_to_modify.replace('a', '4')
new_text1 = new_text.replace('b', '8')
new_text2 = new_text1.replace('l', '1')
new_text3 = new_text2.replace('o', '0')
new_text4 = new_text3.replace('s', '5')
new_text5 = new_text4.replace('t', '7')
print(new_text5)






