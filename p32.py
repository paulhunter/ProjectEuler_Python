'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39x186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Notes: 
I can't think of a nice way to do this. Lets just wing it
'''
import time
import itertools

def main():
	t = time.clock()
	possibleNumbers = itertools.permutations((1,2,3,4,5,6,7,8,9),9)
	result = dict()
	answer = 0
	for number in possibleNumbers:
		for a in range(7):
			for b in range(7-a-1):
				if convertToInt(number[0:a+1]) * convertToInt(number[a+1:a+b+2]) == convertToInt(number[a+b+2:]):
					result[convertToInt(number[a+b+2:])] = True
	for x in result.keys():
		if result[x] == True:
			answer += x

	print "Answer: %d" % answer
	print "Time Taken: %0.3f seconds" % (time.clock()-t)

def convertToInt(tup):
	st = ''
	for i in tup: st+=i.__str__()
	return int(st)


if __name__ == '__main__':
	main()