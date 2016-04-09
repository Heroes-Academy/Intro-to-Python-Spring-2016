"""
I will provide the equations in the comments and you must
write the code that reflects the equations.

I will also specify which variable you should input.
You should write a message indicating what the person is inputting.

I have done the first one for you.
"""

# this is an import for the pi number
# it is used for your questions below
from math import pi

### Area of a Square
# equation: area = side_length ** 2
# input the side length
print("I will calculate the area of a square")
side_length = float(input("Please tell me the side length: "))
area = side_length ** 2
print("The area of a the square with side_length {} is {}".format(side_length, area))

### Area of a Circle
# equation: area = pi * radius**2
# input the radius

### Volume of a Sphere
# equation: area = 4/3 * pi * radius**3
# input the radius

### Weight on Pluto
# explanation:
### if we know how much less gravity a planet has
### then we can calculate our weight on that planet
### pluto has 5% of our gravity, which leads to the equation
# equation: weight_on_pluto = 0.05 * weight_on_earth
# input: your weight on earth



### Bonus
## Given the weight that was input
## Calculate the weights for the other planets.
# Mercury has 38% of our gravity
# Venus has 90%
# The Moon has 16%
# Mars has 38%
# Jupiter has 236%
# Saturn has 108%
# Uranus has 80%
# Nepture has 112%
