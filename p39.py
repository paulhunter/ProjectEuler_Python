'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

notes:
If we can write a method that is fast at finding right angle triangles given a hypotnuse
we can write another wrapping method which finds viable hypotnuses given a perimeter, at
which point we can just try all values from 5 to 1000 (3,4,5) is the smallest right angled
INTEGER length triangle. 
'''

import time
import math

def main():
	t = time.clock()
	maxSols = (0,0)
	for p in range(5,1001):
		s = len(findPS(p))
		maxSols = (p,s) if s > maxSols[1] else maxSols
	print "Answer %d" % maxSols[0]
	print "Time Taken: %0.3f seconds" % (time.clock()-t) 

def findPS(per):
	sols = []
	for h in range(2*per/5, (per/2)+1):
		sols += [s + (h,) for s in findRTS(h) if sum(s + (h,)) == per]
	return sols


# c^2 = a^2+b^2
#find RightTriangleSolution given the hypotnus
def findRTS(hyp):
	solutions = []
	for a in range(1,int(math.sqrt(0.5*hyp*hyp))+1):
		b = math.sqrt((hyp*hyp)-(a*a))
		if b % 1 == 0:
			solutions.append((a,int(b)))
	return solutions

if __name__ == '__main__':
	main()

