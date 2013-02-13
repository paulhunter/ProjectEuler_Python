'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

notes:
this should be relatively easy to do using itertools to create all the perumations. 
Althought it is not noted in this problem, we can assume that the Pandigital definition is that
which was layed out in problem 32, in which each digit is used only once and that a number can't 
start with zero. With a pile of tuples we just need to find a nice way to process them to see
if they meet the criteria. 
'''

import itertools
import time

def main():
	t = time.clock()
	possibleValues = [x for x in itertools.permutations([0,1,2,3,4,5,6,7,8,9],10) if x[0] != 0]
	sum = 0
	for val in possibleValues:
		if isWhatWeWant(val):
			sum += convertToInt(val)

	print "Answer: %d" % sum
	print "Time Taken %0.3f seconds" % (time.clock()-t)

	
def isWhatWeWant(number):
	divisors = [2,3,5,7,11,13,17]
	for i in range(7):
		if convertToInt(number[i+1:i+4]) % divisors[i] != 0:
			return False
	return True

def convertToInt(tup):
	st = ''
	for i in tup: st+=i.__str__()
	return int(st)


	

if __name__ == '__main__':
	main()