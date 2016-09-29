#!/usr/bin/env python2
# coding=utf-8
#
# Name:			gkanapass.py
# Function:		a python based password generator with focus on japanese/kana-style passwords
#               https://en.wikipedia.org/wiki/Kana
#               https://xkcd.com/936/
# Date:			20160929.01
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
appDescription="gkanapass is a python based password generator influenced by kana"
appDevURL="https://github.com/yafp/gkanapass"
appVersion="20160929.02"


#=========================     FUNCTIONS     ===================================
def clearScreen():
	if (os.name == 'posix') or (os.name == 'mac'): # linux or mac
		os.system('clear')
	if os.name == 'nt': # windows
		os.system('cls')


def printHead(title):
	#clearScreen()
	print ("------------------------------------------------")
	print (" \033[1m"+ appName + "\033[0m - (" + appVersion +") - " + title)
	print ("------------------------------------------------\n")
	return;


def validateArguments():
	#print 'Number of arguments:', len(sys.argv), 'arguments.'
	#print 'Argument List:', str(sys.argv)
	
	pwLengthInfo="unset"

	if len(sys.argv) < 2: # no user argument available
		pwLengthInfo="Password length: 10 (default)"
		length="10"				# default length

	elif (sys.argv[1]=="-v"):	# version
		displayVersion()	# display version informations
		sys.exit()

	elif (sys.argv[1]=="-h"):	# help 
		displayHelp()	# display help informations
		sys.exit()

	else: # user entered an argument - check it
		length=sys.argv[1]
		try:
			if int(float(length))>7: # if argument is bigger then 7 -> good
				pwLengthInfo="Password length: "+length
			
			if int(float(length))<8: # check if argument is smaller 8 -> bad
				length="8"		# force to min length
				pwLengthInfo="Password length 8 (forced minimal value)"
		except BaseException:	# invalid parameter (not a number) - jump back to default
			pwLengthInfo="Password length: 10 (forcing default value)"
			length="10"			# default length

	print (pwLengthInfo+"\n")
	return length;


def generateKanaPass(length):

	# define some symbol-pools
	charPoolConsonantKana = ['k','s','t','n','h','m','y','r','w']		# kana consonants
	charPoolConsonantSimilar = ['d','f','l','p','v']					# non-kana consonants
	charPoolVocal = ['a','e','i','o','u']								# vocals
	charPoolNumbers = ['1','2','3','4','5','6','7','8','9','0']			# numbers
	charPoolSpecials = ['#','+','-','_','.','?','!',"&"]				# specials

	for i in range (0,10): # generate 10 passwords
		generatedPassword='' # start with an empty password

		for dummy in range (0,length): # build single_generateRandomPair
			randomNumber=random.randrange(1,100) # generate a random number between 1 and 100 - based on that we randomize the password-generation

			if randomNumber>95: 		# lowercase consonants kana + special
				generatedPassword=generatedPassword+random.choice(charPoolConsonantKana)+random.choice(charPoolSpecials)

			elif randomNumber>90:		# uppercase consonants similar & uppercase vocal
				generatedPassword=generatedPassword+random.choice(charPoolConsonantSimilar).upper()+random.choice(charPoolVocal).upper()

			elif randomNumber>85: 		# uppercase consonants kana + number
				generatedPassword=generatedPassword+random.choice(charPoolConsonantKana).upper()+random.choice(charPoolNumbers)

			elif randomNumber>80: 		# lowercase consonants kana + number
				generatedPassword=generatedPassword+random.choice(charPoolConsonantKana)+random.choice(charPoolNumbers)

			elif randomNumber>75:		# uppercase consonants kana & lowercase vocal
				generatedPassword=generatedPassword+random.choice(charPoolConsonantSimilar).upper()+random.choice(charPoolVocal)

			elif randomNumber>60:		# lowercase consonants similar & lowercase vocal
				generatedPassword=generatedPassword+random.choice(charPoolConsonantSimilar)+random.choice(charPoolVocal)

			elif randomNumber>50:		# lowercase kana similar & uppercase vocal
				generatedPassword=generatedPassword+random.choice(charPoolConsonantSimilar)+random.choice(charPoolVocal).upper()

			else: 						# lowercase consonants kana & lowercase vocal
				generatedPassword=generatedPassword+random.choice(charPoolConsonantKana)+random.choice(charPoolVocal)

		# user-defined password length might be odd
		# generated password is always even and too long -> cut generated to defined length
		generatedPassword=generatedPassword[:int(float(length))]

		# output the generated and cutted password
		print (str(i) + ": " + generatedPassword)


def displayHelp():
	clearScreen()
	printHead("Help")
	print ("ABOUT:")
	print ("\t"+appDescription)
	print ("\t"+appDevURL+"\n")
	print ("CORE:")
	print ("\tpkanapass\tGenerates 10 passwords with default length (10)")
	print ("\tpkanapass 14\tGenerates 10 passwords with user-defined length (14)")
	print ("\nMISC:")
	print ("\tpkanapass -h\tDisplay this help dialog")
	print ("\tpkanapass -v\tDisplay application version")


def displayVersion():
	clearScreen()
	printHead("Version")
	print ("VERSION:")
	print ("\t" + appVersion)


#========================     MAIN SCRIPT     ==================================
clearScreen() # clear the screen
printHead("Passwords") # output a head containing appname, version etc
intLength=int(float(validateArguments())) # validate argument & parse to int
generateKanaPass(intLength)	# Generate 10 passwords with defined length
#==========================     THE END     ====================================
