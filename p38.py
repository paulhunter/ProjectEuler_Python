'''
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

notes:
We just need to write an effecient check to see if we can make a 1-9 Pandigital from a given integer.
Assuming n>2, we know that length(i+i*2) needs to be equal or less than 9 digits, so we can't go above 
9999 as a rough estimate. 
'''

import time

def main():
	t = time.clock()
	maxValue = 0
	for i in range(1,9999):
		result,val = findPDV(i)
		maxValue = maxValue if result == False else max(val,maxValue)
	print "Answer: %d" %maxValue
	print "Time Taken: %0.3f seconds" % (time.clock()-t)

def findPDV(val):
	#We need to find if we can use val to create the digits 1-9, and if we can what
	#is the number we can get out of this. 
	digits = []
	result = 0
	for n in range(1,10):
		for d in (val*n).__str__():
			if d == '0' or d in digits:
				result = -1
				break
			else:
				digits.append(d)
		if result < 0 or len(digits) == 9: 
			if n == 1:
				result = -1
			break
	if result == 0:
		result = convertToInt(digits)
	return (False, 0) if result < 0 else (True, result)


def convertToInt(tup):
	st = ''
	for i in tup: st+=i.__str__()
	return int(st)

if __name__ == '__main__':
	main()