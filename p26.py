#!/usr/bin/python

#Project Euler Problem 26
'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10=	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

From a little bit of research on repeating decimals we know a few things.
One, everyone rational number (Something that can be expressed as an integer over an integer) is either terminating
or have a repeating cycle
This, is extremely important, because we now konw we have to continuely look for a repeat until we find one, or the decimal ends
'''

import re
import time
from decimal import *

reg = re.compile(r"(\d+)\1$")
lengths = [0]*1000
n = Decimal(1)
for d in range(1,1000):
	nd = Decimal(int(d))
	lent = 2
	getcontext().prec = len	
	dec = decimal(1)/decimal(d)
	while(len(dec)==lent):
		match = reg.search(dec)
		if(match != None):
			lengths[d] = lent = 1
			break
		else:
			lent += 2
			getcontext().prec = lent
			dec = str(n/nd)[2:]

for a in range(1,1000):
	print a,":",lengths[a]