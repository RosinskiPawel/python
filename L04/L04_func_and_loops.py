#======6.2=======
#1

def cube(x):
    return pow(int(x), 3)




#=====
#2
def greet():
    name = input("What's your name? ")
    print("Hello", name)
    return
greet()


#=====6.3 Challenge=========

def far_to_cel():
    #This function converts the value in degrees Fahrenheit to Celsius
    
    temp_F = input("Enter a temp. in Fahrenheit ")
    conv_F_to_C = round(((float(temp_F)-32)*5/9), 2)
    print(f"{temp_F} degrees Fahrenheit = {conv_F_to_C} degrees Celsius")

    
def cel_to_far():
    #This function converts the value in degrees Celsius to Fahrenheit
    
    temp_C = input("Enter a temp. in Celsius ")
    conv_C_to_F = round((float(temp_C)*9/5+32), 2)
    print(f"{temp_C} degrees Celsius = {conv_C_to_F} degrees Fahrenheit")

def temp_conv():
    cel_to_far()
    far_to_cel()

#===============

#======6.4====================

#1
for i in range(2, 11):
    print(i)

#2
i = 2
while i<11:
    print(i)
    i=i+1


#3
def doubles(x):
    for i in range(3):
        x = int(x)*2
        print(x)


#====Challenge 6.5===========

def invest():
    
    amount = float(input("input the amount "))
    rate = float(input("input the rate "))
    years = int(input("input the years "))
    
    for i in range(years):
        amount = round((amount + amount*rate), 2)
        print(f"year {i+1}: ${amount}")
        
    
    
    
