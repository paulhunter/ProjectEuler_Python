#!/usr/bin/python

import math
import time
import sys
t = time.clock()

values = []
for i in range(1,10001):
	numfacs = 0
	sq = int(math.sqrt(i))
	for f in range(1,sq):
		if i % f == 0:
			numfacs += f + (i/f)
	if sq*sq == i:
		numfacs += sq
	numfacs -= i
	values.append(numfacs)

	
	
sum = 0
for i in range(len(values)):
	#print "%d : %d" % (i+1, values[i])
	if values[i] < 10001 and i+1 == values[values[i]-1] and not i+1 == values[i]:
		sum += (i+1)
print sum
print "Time :", time.clock()-t