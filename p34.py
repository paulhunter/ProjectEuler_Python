'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Notes: Again, very easy. 
'''

import time

#Upper Limit = 7 * 9! = 2540160

def main():
	t = time.clock()
	print "Answer: %d" % sum([(x if isDigitFactorialNumber(x) else 0) for x in range(3,2540160)])
	print "Time Taken: %0.3f second Execution Time" % (time.clock()-t)

def isDigitFactorialNumber(i):
	return i == sum([fact(int(x)) for x in (i.__str__())[:]])

def fact(x):
	if x <= 1: 
		return 1
	else:
		return x*fact(x-1)

if __name__ == '__main__':
	main()


	