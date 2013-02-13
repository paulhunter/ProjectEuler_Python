'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

notes:
Should be simple enough to just generate a string of the fractional part out to digit 1000000
and do a calculation, it won't be space friendly, but it will work. 
'''

import time

def main():
	t = time.clock()
	st = ''
	dc = 0
	a = 1
	while(dc <= 1000000):
		st += a.__str__()
		dc += len(a.__str__())
		a += 1
	st = '0' + st
	answer = int(st[1])*int(st[10])*int(st[100])*int(st[1000])*int(st[10000])*int(st[100000])*int(st[1000000])
	print "Answer: %d" % answer
	print "Time Taken: %0.3f seconds" % (time.clock()-t)

if __name__ == '__main__':
	main()

