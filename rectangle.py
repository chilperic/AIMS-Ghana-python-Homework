#!/usr/bin/env python
import sys

value = "area = {0}!\nperimeter = {1}!"



if len(sys.argv)!=3:
	print "Wrong input!! provide two values"

else:
	#check if  int or not'3.14'.replace('.','',1).isdigit()
	if sys.argv[1].replace('.','',1).isdigit() ==True and sys.argv[2].replace('.','',1).isdigit()==True: 
		area_value = float(sys.argv[1]) * float(sys.argv[2])
		perimeter_value = 2*float(sys.argv[1]) + 2*float(sys.argv[2])
		print(value.format(area_value,perimeter_value)) 
		
	else:
		print "Wrong input!! enter a positive number!!"
	







