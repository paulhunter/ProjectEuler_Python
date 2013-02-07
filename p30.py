'''
Project Euler Problem 30: Digit Fifth Powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Notes:
What is the maximum possible number that we can form with the fifth power of a numbers digits?
9^5 = 59049
999,999 > 6*59049 = 354294

Bahaha, I think we can do this on one line!
'''
import time
def main():
	t = time.clock()
	print "Answer: %d" % sum([a for a in range(2,999999) if a == sum([int(x)**5 for x in a.__str__()])])
	print "Time Taken: %0.3f seconds." % (time.clock()-t)

if __name__ == '__main__':
	main()