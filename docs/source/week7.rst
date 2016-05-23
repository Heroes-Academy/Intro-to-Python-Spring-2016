Week 07: Advanced Functions and Basic Classes
=============================================

Summary
-------

Important Note: No class next week! Don't come in on Sunday, May 29th. Week 08 resumes on Sunday, June 5th.

This was our final week of all-new material! We covered 2 topics: functions that have **return** statements, and an intro to Python **classes**. Short summary below - more information can be found in the lecture slides.

Functions with Return Statements
********************************
Last week, we only talked about functions that take input arguments and print things. But what if we wanted to write a function that returns a value you can put in a variable?

The answer is a **return** statement. At the end of a function, use a return statement to have the function spit out a particular value. Then, when you call that function, you can put the returned value in some variable. 

Here's an example:
::
	def addition_func(x, y):
		result = x + y
		return result

Then, if you want to call this function, you can do this:
::
	the_sum = addition_func(10, 15)
	
We call the function, and put the return value into the ``the_sum`` variable.

Python Classes
**************
[ Summary coming tomorrow ]


Extra Resources
---------------

[ Resources coming tomorrow ]

Homework
--------

Because we have 2 weeks until next class, try to do this assignment before next Sunday. Then on Sunday, I'll post another assignment for the following week.

For homework this week, you'll be writing another class. You can pick any object you want to write a class for - however, you need to include the following requirements:

1. The class should have at least 3 properties (remember, properties are just internal variables)
2. The properties should include at least one Boolean, at least one String, and at least one Int
3. The class should have at least 2 internal functions
4. At least 1 internal function needs to somehow use a property of the class (remember to use the ``self`` keyword!)
5. At least 1 internal function needs to return a value
6. At least 1 internal function needs to take an input argument
6. The functions and properties should be meaningfully named (for example, no names like "x," "a," or "var")

Then, once you've defined the class, write some code that does the following:

1. Make an object of that class
2. Change one or two of the properties of the class, so they aren't just the default values
3. Call the class's functions

This is mostly just a review of what we covered this week and last week. Next Sunday, the assignment will be a little more complex. 

Remember to send me an email at tmeo@njgifted.org if you have any questions. Good luck!!

Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1bxPpZBtE3FhP1WW_vLRvRaCaI3jUfbWL05ZhDyczNSw/embed?start=false&loop=false&delayms=30000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>