'''
In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).

It is possible to make L2 in the following way:

    1xL1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can L2 be made using any number of coins?

Note:
This is a combinations problem. But, I think we can in a sense do a brute force, kinda?
Recursively? Maybe? SUREEEEE WHY NOT!?
'''

import time

target = 200
coins = [1,2,5,10,20,50,100,200]

def main():
	t = time.clock()
	print "Answer: %d" % nextCoin(0,0)
	print "Time Taken %0.3f seconds" % (time.clock()-t)

#given a running total and an index of the next coin value find the number of
#combinations to the target
def nextCoin(index, runningValue):
	if runningValue == target:
		return 1
	elif runningValue >= target or index >= len(coins):
		return 0
	else:
		count = 0
		for a in range((target-runningValue)/coins[index]+1):
			count += nextCoin(index+1, runningValue + a*coins[index])
		return count

if __name__ == '__main__':
	main()

