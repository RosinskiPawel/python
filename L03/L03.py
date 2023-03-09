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
completedText = firstStr+secondStr
print(completedText)
#OR
print(firstStr+secondStr)

#3
firstStr = "Avo"
secondStr = "Cado"
print(firstStr+" "+secondStr)

#4
str = 'bazinga'
print(str[2:])


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

