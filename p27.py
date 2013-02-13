'''
Euler published the remarkable quadratic formula:
n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
Using computers, the incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
Considering quadratics of the form:
    n^2 + an + b, where |a| < 1000 and |b| < 1000
    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

notes:
A 'brute force' won't take long as long as our check method is decent and aborts as early as possible.
'''

import time
import math

def main():
	t = time.clock()
	primeCat = findPrimes()
	maxTuple = (0,0,0)
	for a in range(-999,1000):
		for b in range(-999,1000):
			result = findNumPrimes(a,b,primeCat)
			if result > maxTuple[2]:
				maxTuple = (a,b,result)

	print "Answer: %d" % (maxTuple[0]*maxTuple[1])
	print "Time Taken: %0.3f seconds" % (time.clock()-t)



def findNumPrimes(a,b,primeCat):
	n = 0
	count = 0
	while(n*n+a*n+b > 0 and primeCat[n*n+a*n+b] == True):
		n += 1
		count += 1
	return count


def findPrimes(limit=1000000):
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

	return catalog



if __name__ == '__main__':
	main()