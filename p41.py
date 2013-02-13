'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

Notes: 
This solution is not the nicest, but I lack a better idea right now. I'll come back to it later. 
'''

import math
import time

def main():
	t = time.clock()
	primes = findPrimes()
	print "Primes Found"

	mp = 0
	for a in range(1,len(primes)):
		if isPD(primes[-a]):
			break
	print "Answer: %d" % primes[-a]
	print "Time Taken: %0.3f seconds" % (time.clock()-t)


def isPD(value):
	n = len(value.__str__())
	digits = []
	for d in value.__str__():
		if int(d) > n or d == '0' or d in digits:
			return False
		digits.append(d)
	return True

def findPrimes(limit=9000000):
	#This is an implementation of the Sieve of Atkin
	components = [(x,y) for x in range(1,int(math.sqrt(limit))+1) for y in range(1,int(math.sqrt(limit))+1)]

	catalog = dict([(1,False),(2,True),(3,True),(4,False)])
	for a in range(5,limit+1):
		catalog[a] = False

	for com in components:
		x,y = com
		n = (4*x*x)+(y*y)
		if(n <= limit and (n % 12 == 1 or n % 12 == 5)):
			catalog[n] = not catalog[n]
		n = (3*x*x)+(y*y)
		if(n <= limit and (n % 12 == 7)):
			catalog[n] = not catalog[n]
		n = (3*x*x)-(y*y)
		if(x>y and (n<= limit) and (n % 12 == 11)):
			catalog[n] = not catalog[n]

	for x in range(5,int(math.sqrt(limit))+1):
		if catalog[x] == True:
			for y in range(x*x,limit+1,x*x):
				catalog[y] = False

	return [x for x in catalog.keys() if catalog[x] == True]

if __name__ == '__main__':
	main()

