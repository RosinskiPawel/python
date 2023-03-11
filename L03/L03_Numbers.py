
#--------5.1------

#1
num1 = 1_234_456_000
num2 = 123456000
print(num1)
print(num2)

#2

num = 175e+3
print(f"{num}")

#3

num = 2e15

#----------5.3 Challenge-----------
 

text1 = "Enter a base: "
base = input(text1)
text2 = "Enter an exponent: "
expo = input(text2)
arith = float(base)**float(expo)
print(f"{base} to the power of {expo} is {arith}")

#-------5.5------
#1
text1 = "Enter a number: "
numb = input(text1)
print(f"{numb} rounded to 2 decimal places is {round(float(numb), 2)}")

#2
text1 = "Enter a number."
numb1 = input(text1)
print(f"The absolute value of {numb1} is {abs(float(numb1))}.")

#3

tex1 = "Enter first number: "
numb1 = input(tex1)
tex2 = "Enter second number: " 
numb2 = input(tex2)
diff = float(numb1) - float(numb2)
print(f"The diference between {numb1} and {numb2} is an integer: {diff.is_integer()}.")
      
#---------5.6---------
#1
n = 3**0.125
print(f"{n:.3f}")

#2
currency = 150000
print(f"{currency:,.2f}")

#3
n = 2/10
print(f"{n:.0%}")

