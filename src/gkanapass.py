#!/usr/bin/env python2
# coding=utf-8
#
# Name:			gkanapass.py
# Function:		Generate Kana-style passwords
#               https://en.wikipedia.org/wiki/Kana
# Date:			20160210
# Author: 		yafp

# https://xkcd.com/936/


# Missing so far for a good random password
#
# - numbers


from functions import validateArguments
from functions import generateKanaPass

intLength=int(float(validateArguments())) # validate argument & parse to int
generateKanaPass(intLength)	# Generate 10 passwords with defined length
