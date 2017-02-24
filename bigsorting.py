#!/bin/python

import sys

n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(unsorted_t)
# your code goes here
integer_array = []
for i in  unsorted:
	integer_array.append(int(i))

def insertionSort(arr):
	i = 0
	while i < len(arr):
		j = i
		while j > 0 and arr[j] < arr[j-1]:
			t = arr[j]
			arr[j] = arr[j-1]
			arr[j-1] = t
			j -= 1
		#j loop end
		i += 1
	return arr
	#i loop end

sorted_ =  insertionSort(integer_array)
for i in sorted_:
	print str(i)
