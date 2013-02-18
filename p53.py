import pstats
import time

t = time.clock()
count = 0
for n in range(20,101):
	for r in range(1,n/2+(1 if n%2==1 else 0)):
		if pstats.nCr(n,r)>1000000:
			count += 2
	if n%2 == 0 and pstats.nCr(n,n/2)>1000000:
		count += 1
print "Answer: %d" % count
print "Time Taken: %0.3f seconds" % (time.clock()-t)
