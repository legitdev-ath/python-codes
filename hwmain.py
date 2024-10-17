#This is my first python code
print("Hello World!")

#Variable : a variable is a random entity which can be assigned a value
#Types of var : Strings, Integers, Floats, Booleans

#For eg :Here first_name is a variable with Atharv as a value written in single/double quotes
first_name = "Atharv "

#Here 'f' is a format string
print(f"My first name is {first_name}")
last_name = "Mojar"
print(f"My last name is {last_name}")

full_name = first_name + last_name
print(f"My full name is {full_name}")

email = "atharvmojar@gmail.com"
print(f"Email : {email}")

#Integers : integers are just whole numbers without any decimals
#NOTE : Integers are not in QUOTES. in quotes = they are string
#For e.g:
age = 20
print(f"My age is {age}")

#Floats : floats are integers with decimal values
#For e.g:
pi = 3.141592653589793
print(f"Pi is {pi}")

#Booleans : True/False (used mostly in if/else or similar)
is_good = False
if is_good:
    print("I am good.")
else:
    print("I am not good.")


