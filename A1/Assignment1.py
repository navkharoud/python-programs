#!/usr/bin/env python
# coding: utf-8

# Navkaran Singh 3119008

# I am taking this course as an elective to learn about data science and add python to my skillset, i am hoping that by the end of this course i will be fluent in python. My main motive to learn python is to use automation and use bots to for certain tasks. Learning datasciecne along the way will also add to my skillset.

# Section 1.9

# Exercise 1.1 
# . It is a good idea to read this book in front of a computer so you can try out the
# examples as you go.
# Whenever you are experimenting with a new feature, you should try to make mistakes. For example,
# in the “Hello, world!” program, what happens if you leave out one of the quotation marks? What if
# you leave out both? What if you spell print wrong?
# This kind of experiment helps you remember what you read; it also helps when you are programming,
# because you get to know what the error messages mean. It is better to make mistakes now and on
# purpose than later and accidentally.
# 1. In a print statement, what happens if you leave out one of the parentheses, or both?
# 2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
# 3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
# 4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011?
# 5. What happens if you have two values with no operator between them?

# 1. Leaving out any of the paranthesis or both them, gives a syntax error and the program doesnt compile, unless youre running python 2 that allowed you to use print function without with paranthesis.
# 2. leaving out one of the paranthesis would give an error that the string literal is unterminated. Leaving out both of them would make it a variable instead of a string if its a single word and would ask if its defined, but anyway it would not run. 
# 3. having a + sign infront of a positive number would result in no change.2++2 would result in 4, similar to 2+2 
# 4. it would result in a syntax error as leading zeros are not permitted in python
# 5. It would give a syntax error.

# Exercise 1.2
# . Start the Python interpreter and use it as a calculator.
# 1. How many seconds are there in 42 minutes 42 seconds?
# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
# 
# predictions: 
# 1. a minute has 60 seconds therefore (42*60)+42 should be the expected reuslt.
# 2. 1.61 km in a mile, therefore 0.62 miles in a km, therefore 0.62*10 = 6.2 miles in 10kms. 
# 3. total seconds = q1 
#    total miles = q2 
#    average speed in miles/seconds = q1/q2
#    average speed in miles/minutes = avg speed in miles/seconds / 60
#    time to run in minutes = 42+42/60 = 42.7 minutes/ 60 = 0.71 hrs
#    time in miles/hr = 6.2/0.71

# In[9]:


##1 
total_seconds = (42*60)+42
print("there are " + str(total_seconds) +" seconds in 42 minutes, 42 seconds")

##2
miles_in_kms = 1/1.61 
total_miles = 10*miles_in_kms
print("there are "+ str(total_miles)+ " miles in 10 kms")

##3 
averageTimeSeconds = total_seconds/total_miles
averageTimeMinutes = averageTimeSeconds/60

totalHours = (total_seconds/60)/60
MilesHours = total_miles/totalHours

print("average speed in miles per hour = " + str(MilesHours))
print("average pace in seconds = " + str(averageTimeSeconds))
print("average pace in mintues = " + str(averageTimeMinutes))


# Section 2.10

# Exercise 2.1
#  Repeating my advice from the previous chapter, whenever you learn a new feature,
# you should try it out in interactive mode and make errors on purpose to see what goes wrong.
# • We’ve seen that n = 42 is legal. What about 42 = n?
# • How about x = y = 1?
# • In some languages every statement ends with a semi-colon, ;. What happens if you put a
# semi-colon at the end of a Python statement?
# • What if you put a period at the end of a statement?
# • In math notation you can multiply x and y like this: xy. What happens if you try that in
# Python?

# 1. It is still illegal as variable is on the left side
# 2. This is legal as we can define multiple variable values in one line
# 3. Python allows semicolons to be used even tho they are not required. (Simple design practise maybe?)
# 4. periods can be used to in variable expression as it changes type from decimal to float, but if used with anyother statement it causes sytax error, as the period is used for dot notaion for objects. 
# 5. xy doesnt work as there is no variable with that name, xy is different from x and y.

# Exercise 2.2
# Practice using the Python interpreter as a calculator:
# 1. The volume of a sphere with radius r is 4/3πr^3. What is the volume of a sphere with radius 5?
# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
# 
# predictions: 
# 1. simple maths formulae with pie = 3.14, 4/3 * 3.14 * 5^3  
# 2. 40% of 24.95 = 9.98 ie discount per book 
#    cost after discount= 14.96 * 60 books = 898.2
#    $3 for deelivery first book, for rest of the 59, it is 0.75 per book therefore 44.25+3.00 = 47.25 for the delivery therefore total = 945.45
# 3. take time in hours
#    start at 6:52 /60
#    easy for 2 mile at 8:15 pace/ 60 *2
#    tempo pace for 3 miles at 7:12/60 *2
#    finished time> 

# In[17]:


##1
r = 5.0
pi = 3.1415
print((4.0/3.0)*pi*r**3)

##2
priceBook = 24.95 
discount = 0.40*priceBook
priceAfter = priceBook-discount 
totalBooksPrice = priceAfter*60 
deliveryFee = 3.0
deliveryRestOfBooks = 59*0.75
totalDelivery = deliveryFee+deliveryRestOfBooks

totalPrice = totalBooksPrice+totalDelivery
print("$"+str(totalPrice))

##3
start_time = 6 + 52 / 60.0
easypace = (8 + 15 / 60.0 ) / 60.0
tempopace = (7 + 12 / 60.0) / 60.0
runtime = 2 * easypace + 3 * tempopace
breakfast_hr = start_time + runtime
breakfast_min = (breakfast_hr-int(breakfast_hr))*60
breakfast_sec= (breakfast_min-int(breakfast_min))*60

print ('Time to get home', int(breakfast_hr), ":",int (breakfast_min),":", int (breakfast_sec) )


# In[ ]:




