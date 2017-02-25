#!/bin/python

import sys

first,last = raw_input().strip().split(' ')
first,last = [long(first),long(last)]
# your code goes here
count = 0
numcount = 0
numcountaux = 0

if first >= 1  and first <= 10**15 and last >= 1 and last <= 10**15 and last - first <= 10**9 and first <= last:
def isprime(n):
	if (n <= 1):
		return False
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

megaprimes = []

for i in range(first,last+1):
	if isprime(i):
		m = i
		while m > 0:
			rem = m % 10
			if isprime(rem):
				numcount += 1
			numcountaux += 1
			m = m / 10
		if numcount == numcountaux:
			megaprimes.append(i)
		numcount = 0
		numcountaux = 0

print(len(megaprimes)) 
