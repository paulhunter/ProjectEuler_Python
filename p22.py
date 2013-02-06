#!/usr/bin/python


import re
import time

t = time.clock()

names = re.compile(r"\"([A-Z]+)\"").findall(open("./names.txt").read())
names.sort()

i = 1
sums = 0
for n in names:
	sums += i*sum(ord(a)-64 for a in n)
	i += 1

print sums
print "Time :",time.clock()-t