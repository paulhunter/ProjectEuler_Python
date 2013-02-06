
#Project Euler Problem 28
'''
Starting with the number 1 and moving to the right in a 
clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the 
diagonals is 101.

What is the sum of the numbers on the diagonals in a 
1001 by 1001 spiral formed in the same way?
'''

'''
NOTES:
There is a very easy pattern to identify when creating this spiral, 
after we create the 1 in the center, we add 2 to it to get 3, which 
is the next diagonal, then add 2 and get 5, 2 -> 7....
You basically get a pattern of adding 2,2,2,2,4,4,4,4,6,6,6,6..... to get
the diagonals. At the end of each sequence of the same number, you have a grid that is 
n+1 x n+1 if n is the number you added. so we just need to do this until we hit the fourth
time we add 1000 and we are done. EZPZ
'''

	# we are going to add val+i, val+i+i, val+i+i+i and val+i+i+i+i before we
	#add to the value of i, so, we can skip an innder loop and use the formula
	#sum += 4*val * 10*i, and then set val to val += 4*i EZPZ

import time
t = time.clock()
sum = 1
i = 2 #Interval
val = 1 #Current diag value we are going to add and our place holder for where we are

while i <= 1000:
	sum += 4*val + 10*i
	val += 4*i
	i += 2

print "Answer: ",sum
print "Time: ",time.clock()-t