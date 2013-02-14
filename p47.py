'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?

Notes:
Create a fast factorization algorithm, keep trying numbers until you get a sequence of 4 that all had 4 prime factors
'''


import time
import math

def main():
	t = time.clock()
	n = 2
	ltup = [fPF(n),fPF(n+1),fPF(n+2),fPF(n+3)]
	while(not distinctFactors(ltup)):
		n+=1
		ltup.append(fPF(n))
		ltup = ltup[1:]

	print "Answer: %d" % (n-3)
	print "Time Taken: %0.3f seconds" % (time.clock()-t)

#findPrimeFactors
def fPF(val):
	result = []
	while val % 2 == 0:
		result.append(2)
		val //= 2

	for i in range(3,int(math.sqrt(val)+1),2):
		if i > val:
			break
		while(val%i == 0):
			result.append(i)
			val //= i
	if val != 1:
		result.append(val)


	return list(set(result))

def distinctFactors(ltup):
	for tup in ltup:
		if len(tup) != 4:
			return False
	return True

if __name__ == '__main__':
	main()

