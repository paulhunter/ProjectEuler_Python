import time

def main():
	t = time.clock()
	count = 0
	for i in range(1,10000):
		if isLychelNumber(i):
			count += 1

	print "Answer: %d" % count
	print "Time Taken: %0.3f seconds" % (time.clock()-t)


def isLychelNumber(x):
	#Is this problem we are told that for every number below ten thousand, it can be seen that the number is palidromic after 
	#less than 50 iterations or, it is lychel.
	for i in range(51):
		x += flipInt(x)
		if isPalidrome(x):
			return False
	return True

def flipInt(x):
	s = x.__str__()
	return int(s[::-1])

def isPalidrome(x):
	array = list(x.__str__())
	if len(array) == 1:
		return True
	firstHalf = array[:len(array)/2]
	secondHalf = (array[len(array)/2+(1 if len(array)%2==1 else 0):])
	secondHalf.reverse()
	return firstHalf == secondHalf

if __name__ == '__main__':
	main()


