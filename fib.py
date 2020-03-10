#!/usr/bin/python 
# -*- coding: utf-8 -*- 
import sys 

last1,last2,result,cntr=1,1,2,4
x = int(sys.argv[1])
if x <= 2: print("1")
elif x==3: print("2")
else:
	while(cntr<=x):
		last2 = last1
		last1 = result
		result = last1+last2
		cntr+=1
	print(result)
