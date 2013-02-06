#Problem 35
#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?

import math
import time

def main():
	t = time.clock()
	catalog = findPrimes(1000000)
	number = 0
	for n,isPrime in catalog.items():
		if isPrime == True:
			isCirc = True
			for y in range(len(str(n))):
				if catalog[int(''.join(list(str(n))[y:] + list(str(n))[:y]))] == False:
					isCirc = False
					break
			if isCirc:
				number += 1

	print "Answer: %d" % number
	print "Time Taken %.3f seconds" % (time.clock()-t)

def findPrimes(limit):
	#This is an implementation of the Sieve of Atkin
	components = [(x,y) for x in range(1,int(math.sqrt(limit))+1) for y in range(1,int(math.sqrt(limit))+1)]

	catalog = dict([(2,True),(3,True),(4,False)])
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
