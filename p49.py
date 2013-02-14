'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

Notes:
With each prime, find all of the permuations that are prime, then find if there are three
that constitute a sequence and that is not (1487,4817,8147)
'''
import p27
import p32
import itertools
import time

def main():
	t = time.clock()
	print "Answer: %s" % findSeq()
	print "Time Taken: %0.3f seconds" % (time.clock()-t)

def findSeq():
	primeCat = p27.findPrimes(9999)
	primes = [x for x in primeCat.keys() if primeCat[x] == True and x>999 and x<10000]
	res = []
	for p in primes:
		res = []
		for t in [x for x in itertools.permutations(p.__str__(),4)]:
			if primeCat[p32.convertToInt(t)] == True and p32.convertToInt(t) != p and len(p32.convertToInt(t).__str__())==4:
				res.append(p32.convertToInt(t))
		for r in res:
			if r in (1487,4817,8147):
				continue
			for s in res:
				if s >= r:
					break
				if (2*r-s) in res:
					st = ''
					for s in (s,r,2*r-s): st+=str(s)
					return st




if __name__ == '__main__':
	main()
