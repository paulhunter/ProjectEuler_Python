'''
Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?

Notes:
We dont even have to write any code for this one, we can do it with combanitorics and a scientific calculor.
If we look at the 2x2 grid we can see that we always take a path that has two rights, 'R' and two downs 'D'
If we look at this problem inductively we find that for and nxn grid all paths will have n 'R's and n 'D's. 
From here it's a simple number of permutations of the total 2n moves. 
Simply its 40! / (20! * 20!) or 137846528820
'''

print 'Answer: 137846528820'
print 'Time Taken: <Done By Hand>'