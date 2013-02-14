'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2x12
15 = 7 + 2x22
21 = 3 + 2x32
25 = 7 + 2x32
27 = 19 + 2x22
33 = 31 + 2x12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

note:
Easy Peasy Lemon Squeezy
'''


import math
import time
def main():
	t = time.clock()
	primeCat = findPrimes()
	primeList = [x for x in primeCat.keys() if primeCat[x] == True]
	n = 9
	while(True):
		if primeCat[n] == False and failsTest(n,primeList):
			break
		n += 2

	print "Answer: %d" % n
	print "Time Taken: %0.3f seconds" % (time.clock()-t)


def failsTest(val, primes):
	for a in primes:
		if a >= val:
			break
		for b in range(int(math.sqrt(val-a)+1)):
			if val < a + 2*b*b:
				break
			if val == a + 2*b*b:
				return False
	return True



def findPrimes(limit=100000):
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


