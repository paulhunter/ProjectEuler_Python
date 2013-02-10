'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

Note:
Should be relatively straight forward
'''

import time

def main():
	t = time.clock()
	sum = 0
	for i in range(1000000):
		if (isPalidrome(i) and isPalidrome(toBinary(i))):
			sum += i
	print "Answer: %d" % sum
	print "Time Taken %0.3f seconds" % (time.clock()-t)

def isPalidrome(x):
	array = list(x.__str__())
	if len(array) == 1:
		return True
	firstHalf = array[:len(array)/2]
	secondHalf = (array[len(array)/2+(1 if len(array)%2==1 else 0):])
	secondHalf.reverse()
	return firstHalf == secondHalf

def toBinary(x):
	return bin(x)[2:]

if __name__ == '__main__':
	main()