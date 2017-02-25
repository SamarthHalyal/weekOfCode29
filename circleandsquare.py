#!/bin/python

import sys

w,h = raw_input().strip().split(' ')
w,h = [int(w),int(h)]
circleX,circleY,r = raw_input().strip().split(' ')
circleX,circleY,r = [int(circleX),int(circleY),int(r)]
x1,y1,x3,y3 = raw_input().strip().split(' ')
x1,y1,x3,y3 = [int(x1),int(y1),int(x3),int(y3)]
# your code goes here

file_ = open("circle.txt","wa")

canvas = []
rad = r
l = abs(x1-x3)
l = l/2
for m,j in enumerate(range(1,h+1)):
	for n,i in enumerate(range(1,w+1)):
			### Square Logic ###
		if n >= x3 and n <= x1 and m >= y3 and m <= y1:
			canvas.append('#')
		elif n >= x3+1 and n <= x1-1 and m >= y3+1 and m <= y1+1:
			canvas.append('#')
		elif n >= x3+1 and n <= x1-1 and m >= y3-1 and m <= y1-1:
			canvas.append('#')
		elif n == x3+l  and m >= y1-l and m <= y1+l:
			canvas.append('#')
			#############
		elif n >= x3+2 and n <= x1-2 and m >= y3+2 and m <= y1+2:
			canvas.append('#')
		elif n >= x3+2 and n <= x1-2 and m >= y3-2 and m <= y1-2:
			canvas.append('#')
			#############
		elif n >= x3+3 and n <= x1-3 and m >= y3+3 and m <= y1+3:
			canvas.append('#')
		elif n >= x3+3 and n <= x1-3 and m >= y3-3 and m <= y1-3:
			canvas.append('#')
			#############
			### Circle logic #####
		elif n >= circleX-rad and n <= circleX+rad and m == circleY:
			canvas.append('#')
		elif m >= circleY-rad and m <= circleY+rad and n == circleX:
			canvas.append('#')
			##############
		elif n >= circleX-rad+1 and n <= circleX+rad-1 and m+1 == circleY:
			canvas.append('#')
		elif m >= circleY-rad+1 and m <= circleY+rad-1 and n+1 == circleX:
			canvas.append('#')
		elif n >= circleX-rad+1 and n <= circleX+rad-1 and m-1 == circleY:
			canvas.append('#')
		elif m >= circleY-rad+1 and m <= circleY+rad-1 and n-1 == circleX:
			canvas.append('#')
			###############
		elif n >= circleX-rad+1 and n <= circleX+rad-1 and m+2 == circleY:
			canvas.append('#')
		elif m >= circleY-rad+1 and m <= circleY+rad-1 and n+2 == circleX:
			canvas.append('#')
		elif n >= circleX-rad+1 and n <= circleX+rad-1 and m-2 == circleY:
			canvas.append('#')
		elif m >= circleY-rad+1 and m <= circleY+rad-1 and n-2 == circleX:
			canvas.append('#')
			###############
		elif n >= circleX-rad+1 and n <= circleX+rad-1 and m+3 == circleY:
			canvas.append('#')
		elif m >= circleY-rad+1 and m <= circleY+rad-1 and n+3 == circleX:
			canvas.append('#')
		elif n >= circleX-rad+1 and n <= circleX+rad-1 and m-3 == circleY:
			canvas.append('#')
		elif m >= circleY-rad+1 and m <= circleY+rad-1 and n-3 == circleX:
			canvas.append('#')
		 	###############	
		else:
			canvas.append('.')
	canvas.append('\n')
for i in canvas:
	file_.write("\b".join(i),)
file_.close()
with open("circle.txt","r") as content_file:
	content = content_file.read()
	print content

