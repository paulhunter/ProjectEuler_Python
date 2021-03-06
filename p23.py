#!/usr/bin/python

#Project Euler Problem 23
#A perfect number is a number for which the sum of its proper divisors is exactly 
#equal to the number. For example, the sum of the proper divisors of 28 would be 
#1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n 
#and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
#that can be written as the sum of two abundant numbers is 24. By mathematical 
#analysis, it can be shown that all integers greater than 28123 can be written 
#as the sum of two abundant numbers. However, this upper limit cannot be reduced 
#any further by analysis even though it is known that the greatest number that 
#cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum 
#of two abundant numbers.

import math
import time
t = time.clock()

abundant = []
for i in range(1,28124):
	sq = int(math.sqrt(i))
	sumFac = 0
	for f in range(1,sq+1):
		if i % f == 0:
			sumFac += (f + (i/f))
	if sq*sq == i:
		sumFac -= sq
	sumFac -= i
	if sumFac > i:
		abundant.append(i)

posSums = [False]*28125
for a in abundant:
	for b in abundant[abundant.index(a):]:
		if a+b <= 28124:
			posSums[a+b]=True
		else: break
sum = 0
for x in range(1,len(posSums)):
	if posSums[x] == False:
		sum += x

print sum
print "Time: ",time.clock()-t