

import itertools

def fiveElementSort(l):
	if len(l) != 5:
		raise ValueError("fiveElementSort only accepts collections of 5 elements")
	else:
		f = l[:]
		if f[0]>f[1]: f[0],f[1]=f[1],f[0]
		if f[2]>f[3]: f[2],f[3]=f[3],f[2]
		if f[1]>f[3]: f[1],f[3],f[0],f[2]=f[3],f[1],f[2],f[0]
		
		a,b,c,d,e = f[0],f[1],f[2],f[3],f[4]

		if e>=b:
			if e<d:
				if c >= b:
					if c < e: 
						return [a,b,c,e,d]
					else: 
						return [a,b,e,c,d]
				else:
					if c < a: 
						return [c,a,b,e,d]
					else: 
						return [a,c,b,e,d]
			else:
				if c>=b: 
					return [a,b,c,d,e]
				else:
					if c<a: 
						return [c,a,b,d,e]
					else: 
						return [a,c,b,d,e]
		else: # e<b
			if e<a:
				if c>=a:
					if c < b: 
						return [e,a,c,b,d]
					else: 
						return [e,a,b,c,d] 
				else:
					if c < e:
						return [c,e,a,b,d]
					else:
						return [e,c,a,b,d]
			else:
				if c>=e:
					if c < b:
						return [a,e,c,b,d]
					else:
						return [a,e,b,c,d]
				else:
					if c<a:
						return [c,a,e,b,d]
					else:
						return [a,c,e,b,d]



def fiveElementSort_test():
	pbs = itertools.permutations([1,2,3,4,5],5)
	counter = 0
	for s in pbs:
		if fiveElementSort(list(s)) != [1,2,3,4,5]:
			print "fiveElementSort failed for input %s" % s.__str__()
			counter += 1
	if counter > 0:
		print "FAILED fiveElementSort"
		print "    Failed %d of %d tests." % (counter, 120)	
	else:
		print "PASS: fiveElementSort "
	return counter

def runTests():
	failTestCount = 0
	failTestCount += fiveElementSort_test()

	print "--------------------------------------------------"
	print "RESULTS: %d Fails" % failTestCount


