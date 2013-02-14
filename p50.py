'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

Note: There has to be a faster way than this. 
'''


import p27
import time

def main():
	t = time.clock()
	print "Answer: %d" % findSumMaxPrime()
	print "Time Taken: %0.3f seconds" % (time.clock()-t)

def findSumMaxPrime():
	limit = 1000000
	primesCat = p27.findPrimes(limit)
	primes = [x for x in primesCat.keys() if primesCat[x] == True]
	sumPrimes = calcPrimeSums(primes)
	lenSP = len(sumPrimes)
	result = 0

	numP = 0
	for i in range(numP,lenSP):
		for j in range(i-numP-1,0,-1):
			if sumPrimes[i] - primes[j] > limit:
				break
			x = sumPrimes[i] - sumPrimes[j]
			if primesCat[x] == True:
				numP = i-j
				result = x
	return result

def calcPrimeSums(primes):
	result = [0]
	for p in primes:
		result.append(p+result[-1])
	return result

if __name__ == '__main__':
	main()


