#!/bin/python

import sys
import math

x,y = raw_input().strip().split(' ')
x,y = [int(x),int(y)]
# your code goes here
x_list = []
y_list = []
count = 0
x_list.append(x)
y_list.append(y)

def isnotpresentX(n):
	for i in x_list:
		if n == i:
			return False
	return True

def isnotpresentY(n):
	for j in y_list:
		if n == j:
			return False
	return True

def notperfectInt(m,n):
	value =  math.sqrt(m ** 2 + n ** 2)
	if 0 < (value - int(value)):
		return True
	else:
		return False

def sumisalmostInt(list1,list2):
	sum_ = 0
	for i,j in zip(list1,list2):
		sum_ +=  math.sqrt(i ** 2 + j ** 2)
	if sum_ - int(sum_) <= 10 ** -12:
		return True 
	else:
		return False 

for i in range(-12,13):
	for j in range(-12,13):
		if isnotpresentX(j):
			if notperfectInt(i,j):
				x_list.append(i)
				y_list.append(j)
				count += 1
			if count == 11 and sumisalmostInt(x_list,y_list):
				count = 0
				for m,n in zip(x_list,y_list):				
					print str(m) + " " + str(n) 

