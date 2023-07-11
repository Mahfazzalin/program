#!/bin/python3

import sys
import time
#import random
from datetime import datetime


def dot():
	return("-"*50)
def dot2():
	return("."*50)
def equal():
	return("="*50)

def typewriter(anime):
	for char in anime:
		sys.stdout.write(char)
		sys.stdout.flush()
	
		if char != "\n":
			time.sleep(0.02)
		else:
			time.sleep(0.2)

def banner():
	dots = dot()
	typewriter(dots)
	ban ="\nMA"+" "*18+"CALCULATOR"+" "*18+"HF\n"
	typewriter(ban)
	typewriter(dots)
	ban1 ="\n1st enter a oparator."+" "*8+"|"+"  use this oparator\nThen enter a number."+" "*9+"|"+"  + - * / ^ sqrt\nAt last enter another number."+"|"+"  for help => -h\n"
	typewriter(ban1)
	typewriter(dots)
	ban2 ="\nCalculator opened at: "
	time = str(datetime.now())
	typewriter(ban2)
	typewriter(time)
	print("\n")
	typewriter(dots)
	ban3 ="\nDo you want more oparator? write 'more'\n"
	typewriter(ban3)
	
banner()

def help():
	eq = equal()
	typewriter(equal())
	helpop = "\n"+" "*20+"Help option"+" "*20 + "\n"
	typewriter(helpop)
	typewriter(equal())
	help = "\n"+" "*4+"use '+' for" +"-"*21 +"addition\n"+" "*4+"use '-' for" +"-"*17 +"substraction\n"+" "*4+"use '*' for" +"-"*21 +"multiply\n"+" "*4+"use '/' for" +"-"*21 +"division\n"+" "*4+"use  '^' 0r '**' for" +"-"*15 +"power\n"+" "*4+"use  'sqrt' for" +"-"*21 +"root\n"+" "*4+"use  '-ht' for" +"-"*12 +"to see history\n"+" "*4+"use 000  for" +"-"*12 +"to clear history\n"+" "*4 + "use -p for" +"-"*5 +" to see developer details\n"+" "*4+"use 'ctrl' + 'c' for "+"-"*4+"exit the program\n"
	typewriter(help)
def doveloper():
	time.sleep(1)
	print("searching . . ..")
	time.sleep(1.5)
	print("searching on https://www.google.com/ . . ..")
	time.sleep(2)
	print("searching on https://www.github.com/ . . ..")
	time.sleep(2)
	print("searching on https://www.facebook.com/ . . ..")
	time.sleep(2)
	print("wait")
	time.sleep(.5)
	fitch = "fitching data\nrearrage data\n\n\n"
	time.sleep(1)
	typewriter(fitch)
	print(dot())
	time.sleep(.1)
	name ="Name: Mahfazzalin Shawon Reza \nGmail: mahfazzalin1@gmail.com \nGithub: https://www.github.com/mahfazzalin \nFacebook: https://www.facebook.com/mahfazzalinshawon.reza\n"
	typewriter(name)
def inputoparator():
	oparator = str(input("Enter your oparator: "))
	return oparator	
def addition(x,y):
	return x+y

def substract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	return x/y

def power(x,y):
	return x**y

def root(x):
	return sqrt(x)

#logical option

try:
	
	def play_again():
		print(dot())
		oparator = inputoparator()
		print(dot())
		
		if ( oparator == "-h"):
			help()
			history = open('history.txt', "a")
			date = str(datetime.now())
			history.write("\n")
			history.write("\n"+ date)
			history.write("\nUser type "+ oparator + " to open help menu.")
			history.close()
				
		#elif ( oparator == "more"):
		#	print(dot())
		#	time.sleep(.1)
		#	print(" "*17+"More Oparator"+" "*20)
		
		elif ( oparator == "-p"):
			doveloper()
		
		
		elif ( oparator == "+"):
			
			try:
				add1 = float(input("Enter your 1st number :"))
				time.sleep(.1)
				add2 = float(input("Enter your 2nd number: "))
				add = addition(add1,add2)
				print("Result: ", add)
				history = open('history.txt', "a")
				date = str(datetime.now())
				history.write("\n")
				history.write("\n"+ date)
				history.write("\n"+str(add1) + oparator + str(add2) + " = "+str(add))
				history.close()
				print(dot())
				
			except ValueError:
				print("please enter number. Not text.")
		
		elif ( oparator == "-"):
		

			try:
				subs1 = float(input("Enter your 1st number: "))
				subs2 = float(input("Enter your 2nd number: "))
				subs = substract(subs1,subs2)
				print("Result: ", subs)
				
				history = open('history.txt', "a")
				date = str(datetime.now())
				history.write("\n")
				history.write("\n"+ date)
				history.write("\n"+str(subs1) + oparator + str(subs2) + " = "+str(subs))
				history.close
				
				print(dot())
				
			except ValueError:
				print("please enter number. Not text.")
		
		elif ( oparator =="*"):
			try:
				mul1 = float(input("Enter your 1st number: "))
				mul2 = float(input("Enter your 2nd number: "))
				mul = multiply(mul1,mul2)
				print("Result: ", mul)
				
				history = open('history.txt', "a")
				date = str(datetime.now())
				history.write("\n")
				history.write("\n"+ date)
				history.write("\n"+str(mul1) + oparator + str(mul2) + " = "+str(mul))
				history.close
				
				print(dot())
				
			except ValueError:
				print("please enter number. Not text.")
		
		elif ( oparator == "/"):
			try:
				div1 = float(input("Enter your 1st number: "))
				div2 = float(input("Enter your 2nd number: "))
				div = divide(div1,div2)
				print("Result: ", div)
				
				history = open('history.txt', "a")
				date = str(datetime.now())
				history.write("\n")
				history.write("\n"+ date)
				history.write("\n"+str(div1) + oparator + str(div2) + " = "+str(div))
				history.close()
				
				print(dot())
			
			except ValueError:
				print("please enter number. Not text.")
		#this part is for clear the history.
		elif ( oparator == "000"):
				history = open('history.txt', "w")
				date = str(datetime.now())
				history.write("at time: " + date +" : User type "+ oparator + " to clear history.")
				history.close()
				
				
		elif ( oparator =="-ht"):
		
			try:
				
				#history = open('history.txt', "a")
				#date = str(datetime.now())
				#history.write("\n"+ dot())
				#history.write("\n"+ date)
				#history.write("\n"+ dot())
				#history.write("\nUser type "+ oparator + " to see history.")
				#history.close
				
				history = open('history.txt')
				print(history.read())
				history.close()
				
		
			except ValueError :
				print("ValueError")
		elif ( oparator == "^" or "**"):
			try:
				pow1 = int(input("Enter your 1st number: "))
				pow2 = int(input("Enter your 2nd number: "))
				pow3 = power(pow1,pow2)
				print("Result: ", pow3)
				
				history = open('history.txt', "a")
				date = str(datetime.now())
				history.write("\n")
				history.write("\n"+ date)
				history.write("\n"+str(pow1) + oparator + str(pow2) + " = "+str(pow3))
				history.close()
				
				print(dot())
			except ValueError:
				print("please enter number. Not float or text.")
		
		
		else:
			print("Please enter a valid oparator. ")
		restart = play_again()
		return restart
		
	play_again()
	
except KeyboardInterrupt:
	print("\n Exiting program. You are closing the program")
	sys.exit()
