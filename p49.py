'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

Notes:
We can save time by only checking the differences of primes after generating primes up to 9999
which is the largest 4 digit number. From there we can then check each 4 digit prime with 
the 4 digit primes that are less than themselves to find if their next term would be prime. 
'''
import p27
import time

def main():
	t = time.clock()
	print "Answer: %d" % findSeq()[0]
	print "Time Taken: %0.3f seconds" % (time.clock()-t)

def findSeq():
	primeCat = p27.findPrimes(9999)
	primes = [x for x in primeCat.keys() if primeCat[x] == True and x>999 and x<10000]
	for p in primes:
		for q in primes:
			if q>=p:
				break
			elif 2*p-q>9999:
				continue
			elif primeCat[2*p-q] == True:
				return (q,p,2*p-q)

if __name__ == '__main__':
	main()
