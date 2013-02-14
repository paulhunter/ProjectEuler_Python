'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

Note: Pretty sure this is a single liner
'''
import time
t = time.clock()
print "Answer: %s" % ((sum([x**x for x in range(1,1001)])).__str__()[-10:])
print "Time Taken: %0.3f seconds" % (time.clock()-t)