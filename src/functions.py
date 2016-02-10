#!/usr/bin/env python2
# coding=utf-8
#
# Name:			functions.py
# Function:		Defines the functions for gkanapass.py
# Date:			20160210
# Author: 		yafp

import sys		# for handling arguments
import random


# --------------------------------------------------------------------
# validate the arguments
# --------------------------------------------------------------------
def validateArguments():
	#print 'Number of arguments:', len(sys.argv), 'arguments.'
	#print 'Argument List:', str(sys.argv)

	if len(sys.argv) < 2: # no user defined length available
		print("- Setting password length to default (10)")
		length="10"
		#sys.exit('Usage: %s database-name' % sys.argv[0])

	else: # user entered an argument - check it
		length=sys.argv[1]
		print("- Setting password length (" + length +")")

		if int(float(length))<8: # check if argument is smaller 8
			print("- Forcing min password length (8)")
			length="8"

	return length;



# --------------------------------------------------------------------
# generate a password
# --------------------------------------------------------------------
def generateKanaPass(length):

	print "\nPasswords:"
	# define possible symbols
	#charsPureKana = ['k','s','t','n','h','m','y','r','w']
	charsPureKana = ['k','s','t','n','h','m','y','r','w','K','S','T','N','H','M','Y','R','W']
	#charsNonPureKana = ['k','s','t','n','h','m','y','r','w','K','S','T','N','H','M','Y','R','W','d','f','l','p','v','D','F','L','P','V']

	#charsPureVocal = ['a','e','i','o','u']
	charsPureVocal = ['a','e','i','o','u','A','E','I','O','U']


	#charsVocalNumbers = ['a','e','i','o','u','A','E','I','O','U','1','2','3','4','5','6','7','8','9','0']

	for i in range (1,11): # generate 10 passwords
		generatedPassword=''
		for num in range (0,length): # build single password
			generatedPassword=generatedPassword+random.choice(charsPureKana)+random.choice(charsPureVocal)


		# hack: user-defined length might be odd -> generated password is always even -> cut to defined length
		#intLength=int(float(length))
		generatedPassword=generatedPassword[:int(float(length))]
		print str(i) + ":\t" + generatedPassword
