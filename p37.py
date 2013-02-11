
'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Notes:
We should be able to use the Sieve of Atkin again to create a large number primes
and then check them for the ability to truncate them. 
'''

import time
import math


def main():
	t = time.clock()
	hvts = []
	cat = sumPrimes()
	for x in  [ab for ab in cat.keys()[10:] if cat[ab]==True]:
		isWhatWeWant = True
		for a in ([int((x.__str__()[i:])) for i in range(1,len(x.__str__()))]+[int((x.__str__()[:-i])) for i in range(1,len(x.__str__()))]):
			if cat[a] == False:
				isWhatWeWant = False
				break
		if isWhatWeWant == True:
			hvts.append(x)
		if len(hvts) == 11:
			break
	if len(hvts) == 11:
		print "Answer: %d" % sum(hvts)
		print "Time Taken %0.3f seconds" % (time.clock()-t)
	else:
		print "Didn't manage to find 11 :("

def sumPrimes():
	#This is an implementation of the Sieve of Atkin
	limit = 740000
	components = [(x,y) for x in range(1,int(math.sqrt(limit))+1) for y in range(1,int(math.sqrt(limit))+1)]

	catalog = dict([(0,False),(1,False),(2,True),(3,True),(4,False)])
	for a in range(5,limit+1):
		catalog[a] = False

	for x,y in components:
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