
import time

def main():
	t = time.clock()
	print "Answer: %d" % findFibTerms()
	print "Time Taken: %0.6f seconds" % (time.clock()-t)

def findFibTerms(limit = 4000000):
	fibDict = dict()
	fibDict[1] = 1
	fibDict[2] = 2
	s = 2
	n = 3
	while(True):
		fibDict[n] = fibDict[n-1] + fibDict[n-2]
		if fibDict[n] % 2 == 0:
			s += fibDict[n]
		if fibDict[n] > limit:
			break
		n+=1

	return s

if __name__ == '__main__':
	main()

