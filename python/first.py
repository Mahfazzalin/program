#!/bin/python3

#STRINGS
print("hello world")
print('hello world')
print("""this string runs 
multiple lines!""") #triple qoute for multiple line
print("this string is "+" awesome!") #we can also concatenate
print('\n') #new line
print('Test that new line out.')


print('\n')
#MATH
print(50 + 50) #add
print(50 - 50) #substract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #pemdas
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left overs
print(50 / 6) #division with remainder  (or a float)
print(50 // 6) #no remainder

print('\n')
#VARIABLES AND METHODS 

quote = 'All is fair in love and war.'
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters

name = "Mahfazzalin Shawon Reza" #string
age = 22 #int
gpa = 3.36 #float - has a decimal

print(int(age))
print(int(30.1)) 
print(int(30.9)) #will it round? NO.

print("My name is " + name + " and I am " + str(age) + " years old")

age += 1
print(age)

birthday = 1 
age += birthday
print(age)


print('\n')
#FUNCTIONS

def who_am_i(): #this is a function without parameters
	name = "Mahfazzalin Shawon Reza"
	age = 22
	print("My name is " + name + " and I am " + str(age) + " years old")

who_am_i()

def add_one_hundred(num):
	print(num + 100)

add_one_hundred(150)

def add(x,y):
	print(x + y)
	
add(7,7)

def multiply(x,y):
	return x * y

multipication = multiply(7,7)
print(multipication)


