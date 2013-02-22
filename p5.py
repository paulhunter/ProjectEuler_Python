'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

note: This is relatively easy, we just find the highest power of each prime for each factorization of the numbers 1 - 20
1 = 1
2 = 2
3 = 3
4 = 2^2
5 = 5
6 = 2*3
7 = 7
8 = 2^3
9 = 3^2
10 = 2*5
11 = 11
12 = 2^2 * 3
13 = 13
14 = 2*7
15 = 3*5
16 = 2^4
17 = 17
18 = 2*3^3
19 = 19
20 = 2^2 * 5

From the list above we see that our prime factors are then
2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560
EZPZ
'''
print "Answer: 232792560"
print "Time Taken: <Done By Hand>"
