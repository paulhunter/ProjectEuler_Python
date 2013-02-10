

import time

def main():
	t = time.clock()
	sum = 0
	for i in range(2,1000000):
		if (isPalidrome(i) and isPalidrome(toBinary(i))):
			sum += i
	print "Answer: %d" % sum
	print "Time Taken %0.3f seconds" % (time.clock()-t)

def isPalidrome(x):
	array = list(x.__str__())
	if len(array) == 1:
		return True
	firstHalf = array[:len(array)/2]
	secondHalf = (array[len(array)/2:])
	secondHalf.reverse()
	return firstHalf == secondHalf

def toBinary(x):
	return bin(x)[2:]

if __name__ == '__main__':
	main()