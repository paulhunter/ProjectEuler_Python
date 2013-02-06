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
'''
New idea for a algorithm
We generate the decimal out to some number of digits (100 maybe?)
x = 0.29321857291857291857.....
Then we look at everyone past the decimal
x = 2932187291857291857.....
	s   e 
And we start and pick an end to a section
Then we look at the character to the right of the end, in this case 8, and you see if it matches
some amount from the front (s, 2 in this place) and if it doesn't you move your end ahead by one
We keep doing this until the len of s-e exceeds the number of characters after e to the end of the 
string we have. When this happens we take the current longest repition and throw it in max holder

'''


import time
from decimal import *

def main():
	t = time.clock()
	getcontext().prec = 100
	print "Answer: %d" % max([(findMaxRepLength(d),d) for d in range(2,1000)])[1]
	print "Time Taken: %3.3f seconds." % (time.clock()-t)

def findMaxRepLength(denom):
	digits = list((Decimal(1)/Decimal(denom)).__str__()[2:][:-2])
	length = len(digits)
	maxLength = 0
	maxStart = 0
	for start,end in [(x,y) for x in range(0,length) for y in range(x,length/2)]:
		repeat = False
		subLength = end - start + 1 #also the length of the substring we are attempting to match to.

		q = digits[start]
		for i in range(1,subLength):
			if digits[start + i] != q:
				repeat = True
				break
		if repeat == False and subLength != 1:
			continue
		repeat = True
		for i in range(subLength): #For each character in the substring:
			for j in range(1,(length-start)/(subLength)): #Check each tandem sequence's corresponding character. 
				if digits[start+i] != digits[start+(j*subLength)+i]: #break if it does not match and set the flag to abort
					repeat = False
					break
			#If we're still a possible repeat, check the possible tail to ensure it matches
			if repeat != False and length%subLength != 0: #only check if there is no abort flag and a tail exists
				offset = length-((length-start)%subLength)
				for k in range(((length-start)%subLength)): #check only the length of the tail into the sequence
					if digits[start + k] != digits[offset + k]: #if any don't match abort
						repeat = False
						break
			if repeat == False:
				break
		if repeat == True and (((start-maxStart)%maxLength!=0 and subLength != maxLength) if maxLength != 0 else True):
			maxLength = max(subLength, maxLength)
			maxStart = start
			#print '0.'+''.join(digits)
			#print "maxLength updated to %d. Start %d" % (maxLength,start)
			#print maxSeq
			getcontext().prec = 100
			break
	if maxLength == 0 and length == getcontext().prec:
		getcontext().prec += 500
		return findMaxRepLength(denom)
	else:	
		return maxLength

if __name__ == '__main__':
	main()
