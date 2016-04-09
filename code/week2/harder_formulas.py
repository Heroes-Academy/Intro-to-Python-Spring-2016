"""
I will provide a description of a problem.
It is your job to convert that description into a formula.
Then, you must code that formula into an equation and code.

Each of the problems will require an input that I specify.
Write an intro print statement explaining the situation for the problem.
Then write an input statement to get the relevant information.
Finally, use your equation to calculate the answer.
Then, print out the answer in a nice way.

I have completed the first one as an example.

"""

### Luke's Rabbits
# Luke loves his rabbits.
# However, they are breeding like crazy.
# Currently, he has 7 rabbits. Every month, they double.  So next month he will have 14.
# Feeding each rabbit costs $10 dollars a month.
#
# The input should be how many months Luke wants to breed his rabbits.
# The output should be how much month it would cost to feed all of those rabbits that month.

print("""Every month, the number of rabbits doubles.
          If you tell me how many months you want to breed the rabbits,
          then I will calculate how much money it will cost in food""")
num_months = int(input("Number of months: "))
# since it doubles every month, then 7 * 2  is the first month, 7 * 2 * 2 is the second
# so, it is 7 * 2 ** num_months
num_rabbits = 7 * 2 ** num_months
food_cost = 10*num_rabbits
print("It will cost you {} dollars to feed your rabbits that month".format(food_cost))

# this will separate the problems when printing them so they aren't so jumbled
print("=-"*30)

### Bill's Money
# Bill wants to know how much money he can earn from saving.
# He has an investment account that gives him 10% every month
# He wants to know how much month he will have after 1, 3, and 6 months
#
# The input should be how much money he wants to invest.
# The output should be the numbers for each of the 3 lengths of time.

### Sara's Army
# Sara wants to hire an army.
# It will cost her $500 per soldier.
#
# The input should be the amount of money that Sara has
# The output should be the number of soldiers she can get.
#
# Note that the amount of money she has may not be exactly the amount of a soldier
# For example, if she has $700 dollars, she can only get 1 soldier
# So, you will have to do floor division.
# See the slides if you forgot how
