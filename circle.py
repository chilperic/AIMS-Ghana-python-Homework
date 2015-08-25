#!/usr/bin/env python
import sys
import math

value = "area = {0}!\nperimeter = {1}!"

if len(sys.argv)!=2:
	print "Wrong input!! provide just one value"

else:
	#check if  int or not
	if sys.argv[1].replace('.','',1).isdigit() ==True:
		area_value = math.pi * float(sys.argv[1]) * float(sys.argv[1])
		perimeter_value = 2*math.pi*float(sys.argv[1])
		print(value.format(area_value,perimeter_value)) 
	else:
		print "Wrong input!! enter a positive number!!"
	

