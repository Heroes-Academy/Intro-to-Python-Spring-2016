"""
The following exercises will combine the input function and if statements.

The combination fo these two features of Python is really powerful.
I will provide extra directions for each of the exercises.
I have also completed the first one.
"""


### A Menu
# You can use input and if statements to create a menu for users
# The only thing that is required is a consistency between what you tell
# your users to input and what you check for with the if statement.

print("Welcome to my menu!")
print("Enter the number of the thing you want to do.")
print("1. See cool ascii art")
print("2. Hear a joke")
print("3. Leave the program")
their_choice = int(input("Please your choice (1,2, or 3): "))
if their_choice == 1:
    print(""" Here you go!
            ;     /        ,--.
           ["]   ["]  ,<  |__**|
          /[_]\  [~]\/    |//  |
           ] [   OOO      /o|__|    """)
elif their_choice == 2:
    print("Why can't you trust atoms?")
    print("Because they make up everything!")
elif their_choice == 3:
    print("Okay.  Bye!")
else:
    print("I have no idea what you type.. but it wasn't 1, 2, or 3")


### Password checker
# Make a log in system
# Ask the user for the password to log in
# If it's the right password, then tell them it was successful!
# If it's not the right password, give them a failure message.

### Personalized Greeter
# Ask the user for their name
# Check if their name is your name
# If it's you, then put a personalized message
# You can use 'elif' and check if it is other names as well
# You can put personalized messages for them too!
# If it's not any of the names you check for, have a default message in the else


