#!/bin/python

import sys

compare_list = []
whole_compare_list = []
integer_list = []
i_list = []
num_list = []
pi = 3.1415926535897932384626433832795028841971693993751
min,max = raw_input().strip().split(' ')
min,max = [long(min),long(max)]
# your code goes here
def find_nearest(arr, value):
	aux_arr = []
	for i in arr:	
		aux_arr.append(abs(i-value))
	small = aux_arr[len(aux_arr)-1]
	for j in aux_arr:
		if j < small:
			small = j
	idx = aux_arr.index(small)
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
