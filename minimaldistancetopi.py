#!/bin/python

import sys
import numpy as np

compare_list = []
whole_compare_list = []
integer_list = []
i_list = []
num_list = []
pi = 3.1415926535897932384626433832795028841971693993751
min,max = raw_input().strip().split(' ')
min,max = [long(min),long(max)]
# your code goes here
def find_nearest(array, value):
	array = np.array(array)
	idx = (np.abs(array-value)).argmin()
	return idx

if min >= 1 and min <= 10 ** 15 and max >= 1 and max <= 10 ** 15 and min <= max:	
	for i in range(min,max+1):
		i_list.append(i)
		num = pi * i #6535897932384626433832795028841971693993751 * i
		integer_list.append(int(num)) 
		compare_list.append(int(num)/float(i))
		num1 = num + 1
		integer_list.append(int(num1))
		compare_list.append(int(num1)/float(i))
		idx = find_nearest(compare_list,pi)
		num = integer_list[idx]
		num_list.append(num)
		whole_compare_list.append(abs((num/float(i)) - pi))
		integer_list = []
		compare_list = []
	small = whole_compare_list[len(whole_compare_list)-1]
	for i in whole_compare_list:
		if i < small:
			small = i
	idx = whole_compare_list.index(small)
	print str(num_list[idx]) + "/" + str(i_list[idx])
