

import time
import math

def main():
	t = time.clock()
	numTot = 1
	demTot = 1
	mf = 0
	for num in range(10,100):
		for dem in range(num+1,100):
			if isCrazy(num,dem):
				numTot *= num
				demTot *= dem
				mf = max([numTot, demTot, mf])
	n,d = reduceFraction((numTot,demTot),mf)

	print "Answer: %d" % d
	print "Time Taken: %0.3f seconds" % (time.clock()-t)


#Optimized reduceFraction method given the maximum Factor the contributed to either the numerator or denominator
def reduceFraction(fraction,maxFactor):
	n,d = fraction
	for f in range(2,maxFactor+1):
		if f > max([n,d]):
			break
		while(n % f == 0 and d % f==0):
			n /= f
			d /= f
	return (n,d)




#the condition that makes the cancellation special and one of the only four. 
def isCrazy(num,dem):
	val = 1.0*num/dem
	if int(dem.__str__()[0]) != 0 and val == 1.0*int(num.__str__()[1])/int(dem.__str__()[0]):
		if int(num.__str__()[0]) == int(dem.__str__()[1]):
			return True
	if int(dem.__str__()[1]) != 0 and val == 1.0*int(num.__str__()[0])/int(dem.__str__()[1]):
		if int(num.__str__()[1]) == int(dem.__str__()[0]):
			return True

	return False


if __name__ == '__main__':
	main()