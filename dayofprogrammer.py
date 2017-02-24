import sys

y = int(raw_input().strip())

not_leap_list = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_list = [31,29,31,30,31,30,31,31,30,31,30,31]
transition_year_list = [31,15,31,30,31,30,31,31,30,31,30,31]

if y >= 1700 and y <= 2700:
	count = 1
	date = 0
	month = 1
	i = 0
	
	#day of programmer according to Julian calender
	if y % 4 == 0 and y <= 1917:
		while count <= 256:	
			date += 1
			if date >= leap_list[i] and i < (len(leap_list) - 1):
				date = 0
				month += 1
				i += 1
			count += 1
	elif y <= 1917:
		while count <= 256:
			date += 1
			if date >= not_leap_list[i] and i < (len(not_leap_list) - 1):
				date = 0
				month += 1
				i += 1
			count += 1
	
	# year 1918
	if y == 1918:
		while count <= 256:
			date += 1
			if date >= transition_year_list[i] and i < (len(transition_year_list) - 1):
				date = 0
				month += 1
				i += 1
			count += 1
				

	#day of programmer according to Gregorian calender 
	if y % 400 == 0 or y % 4 == 0 and y % 100 != 0 and y >= 1919:
		while count <= 256:	
			date += 1
			if date >= leap_list[i] and i < (len(leap_list) - 1):
				date = 0
				month += 1
				i += 1
			count += 1
	elif y >= 1919:
		while count <= 256:
			date += 1
			if date >= not_leap_list[i] and i < (len(not_leap_list) - 1):
				date = 0
				month += 1
				i += 1
			count += 1


	print str(date) + ".0" + str(month) + "." + str(y)
else:
	print "Out of time travel range!"
