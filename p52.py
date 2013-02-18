
import time

def main():
	t = time.clock()
	n = 101
	while(not checkForMultiples(n)):
		if n >= 10**len(n.__str__())/6:
			n = 10**(len(n.__str__()))+1
		n+=1
	print "Answer: %d" % n
	print "Time Taken: %0.3f seconds" % (time.clock()-t)


def checkForMultiples(x):
	digs =[int(a) for a in x.__str__()]
	for i in range(2,7):
		ds = []
		if len((i*x).__str__()) != len(digs): return False
		for a in (i*x).__str__():
			if int(a) not in digs: return False
			ds.append(int(a))
		if sum(ds) != sum(digs): return False
	return True

if __name__ == '__main__':
	main()

