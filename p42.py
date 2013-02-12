'''
The nth term of the sequence of triangle numbers is given by, tn = (1/2)n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

note:
Find the longest word in file, and then find all the triangular numbers less than len(maxWord)*26 
which is the maximum value of the word. Then just run through all the words and count the ones that are right
'''

import time

def main():
	t = time.clock()
	f = open('p42Data.txt', 'r')
	words = [x.strip('"') for x in f.read().split(',')]
	triLimit = max([len(x) for x in words])*26
	triDict = findTriangularNumbers(triLimit)
	count = sum([(1 if triDict[wordScore(word)] == True else 0) for word in words])
	print "Answer: %d" % count
	print "Time Taken: %0.3f seconds" % (time.clock()-t) 

#calculate triangular numbers up to the limit
def findTriangularNumbers(limit):
	cat = dict()
	for a in range(limit+1):
		cat[a] = False
	n = 1
	term = 0.5*n*(n+1)
	while (term <= limit):
		cat[term] = True
		n += 1
		term = 0.5*n*(n+1)

	return cat

def wordScore(word):
	return sum([(ord(x)-64) for x in word.upper()])

if __name__ == '__main__':
	main()




