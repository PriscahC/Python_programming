# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
word = "What doesn't kill you makes you stronger"
print(word)             #printing output with python

name = input("What is your team name? ")        #obtaining input from user
print("You are most welcome team " + name + " !")   #concatenation

    #----------------------------------------------------------------------------------------------------#

First = input("First Number ")
Second = input ("Enter second number ")
sum = int(First) + int(Second)      #int() converts string to interger
print("the sum is", sum)

    #----------------------------------------------------------------------------------------------------#

#if elif statements
age = int(input("Age "))
if age < 18:
    print("Your age is below adult age")
elif age > 18 and age < 35:
    print("You are a youth")
elif age > 35:
    print("You are above the age limit")
print("Done")

    #----------------------------------------------------------------------------------------------------#

#converter
weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == 'L':         #converts input to upper case, 
    print("Weight in lbs: ", weight / 2 ,"lbs")
else:
    print("Weight in kg: ", weight * 2, "kgs")

    #----------------------------------------------------------------------------------------------------#

#while statement
i = 0
while i < 10:
    print("Hello")
    i += 1          #prints Hello 10x

    #----------------------------------------------------------------------------------------------------#

#methods  append, insert, remove, clear
name = ['one', 'two', 'three', 'four', 'five']
name.append('six')
print(name)
#print(name[0:3])
name.insert(0,'zero')       #at index 0 insert zero
print(name)
name.remove('four')      #remove value, not index
print(name)
print('four' in name)       #returns true if four is found and false if it is not 
print(len(name))        #length of name
name.clear()        #clears array
print(name)

    #----------------------------------------------------------------------------------------------------#

#for loop
salute = "Hello world"
for item in salute:     #loops through the salute
    print(item)         #prints each letter
#numbers = range(5)     #prints  to 5
#numbers = range(5, 10)     #prints 5 to 10
numbers = range(5, 10, 2)       #prints 5 to 10, with a gap of 2
for number in numbers:
#for number in range(5)
    print(number)

#functions