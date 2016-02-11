#!/usr/bin/env python2
# coding=utf-8
#
# Name:			gkanapass.py
# Function:		a python based password generator with focus on japanese/kana-style passwords
#               https://en.wikipedia.org/wiki/Kana
#               https://xkcd.com/936/
# Date:			20160211
# Author: 		yafp


# todo
# - add try & except blocks
# - harden parameter validation


#==========================     IMPORT     =====================================
import random		# for randomness
import os			# for clearing the screen
import sys			# for handling arguments
#import argparse	# better argument parsing
					# https://stackoverflow.com/questions/4188467/how-to-check-if-an-argument-from-commandline-has-been-set


#=========================     VARIABLES     ===================================
appName="gkanapass"
appVersion="20160211.01"


#=========================     FUNCTIONS     ===================================
def clearScreen():
	if (os.name == 'posix') or (os.name == 'mac'): # linux or mac
		os.system('clear')
	if os.name == 'nt': # windows
		os.system('cls')


def printHead(str):
	clearScreen()
	print ("------------------------------------------------")
	print (" \033[1m"+ appName + "\033[0m - (" + appVersion +") - " + str)
	print ("------------------------------------------------\n")
	return;


def validateArguments():
	#print 'Number of arguments:', len(sys.argv), 'arguments.'
	#print 'Argument List:', str(sys.argv)

	if len(sys.argv) < 2: # no user argument available
		length="10"

	elif (sys.argv[1]=="-v"):
		displayVersion()
		sys.exit()

	elif (sys.argv[1]=="-h"):
		displayHelp()
		sys.exit()

	else: # user entered an argument - check it
		length=sys.argv[1]
		try:
			if int(float(length))<8: # check if argument is smaller 8
				length="8"
		except:	# invalid parameter (not a number) - jump back to default
			length="10"

	return length;


def generateKanaPass(length):
	printHead("Generated passwords")
	print (" Length: "+str(length)+"\n")

	# define some symbol-pools
	charPoolConsonantKana = ['k','s','t','n','h','m','y','r','w']		# kana consonants
	charPoolConsonantSimilar = ['d','f','l','p','v']					# non-kana consonants
	charPoolVocal = ['a','e','i','o','u']								# vocals
	charPoolNumbers = ['1','2','3','4','5','6','7','8','9','0']			# numbers
	charPoolSpecials = ['#','+','-','_','.','?','!',"&"]				# specials


	for i in range (1,11): # generate 10 passwords
		generatedPassword='' # start with an empty password

		for num in range (0,length): # build single passwords
			randomNumber=random.randrange(1,100) # generate a random number between 1 and 100 - based on that we randomize the password-generation

			if randomNumber>90: 		# lowercase consonants kana + special
				generatedPassword=generatedPassword+random.choice(charPoolConsonantKana)+random.choice(charPoolSpecials)

			#elif randomNumber>90: 		# uppercase consonants kana + number
				#generatedPassword=generatedPassword+random.choice(charPoolConsonantKana).upper()+random.choice(charPoolNumbers)

			elif randomNumber>85: 		# lowercase consonants kana + number
				generatedPassword=generatedPassword+random.choice(charPoolConsonantKana)+random.choice(charPoolNumbers)

			#elif randomNumber>80:		# lowercase consonants similar & lowercase vocal
				#generatedPassword=generatedPassword+random.choice(charPoolConsonantSimilar)+random.choice(charPoolVocal)

			elif randomNumber>80:		# lowercase kana similar & uppercase vocal
				generatedPassword=generatedPassword+random.choice(charPoolConsonantSimilar)+random.choice(charPoolVocal).upper()

			elif randomNumber>75:		# uppercase consonants kana & lowercase vocal
				generatedPassword=generatedPassword+random.choice(charPoolConsonantSimilar).upper()+random.choice(charPoolVocal)

			#elif randomNumber>65:		# uppercase consonants similar & uppercase vocal
				#generatedPassword=generatedPassword+random.choice(charPoolConsonantSimilar).upper()+random.choice(charPoolVocal).upper()

			else: 						# lowercase consonants kana & lowercase vocal
				generatedPassword=generatedPassword+random.choice(charPoolConsonantKana)+random.choice(charPoolVocal)

		# hack:
		# user-defined length might be odd
		# generated password is always even and too long
		# -> cut to defined length
		generatedPassword=generatedPassword[:int(float(length))]

		# output the generated password
		print (" " + generatedPassword)


def displayHelp():
	printHead("Help")
	print ("CORE:")
	print ("./pkanapass\t\tGenerates 10 passwords with default length (10)")
	print ("./pkanapass 14\t\tGenerates 10 passwords with user-defined length (14)")
	print ("\nMISC:")
	print ("./pkanapass -h\t\tDisplay this help dialog")
	print ("./pkanapass -v\t\tDisplay application version")


def displayVersion():
	printHead("Version")
	print ("Version: " + appVersion)


#========================     MAIN SCRIPT     ==================================
intLength=int(float(validateArguments())) # validate argument & parse to int
generateKanaPass(intLength)	# Generate 10 passwords with defined length
#==========================     THE END     ====================================
