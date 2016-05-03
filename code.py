#!/usr/bin/python


fo = open("route", "r")

str=fo.read()

dict=eval(str);

for obj in dict:
	print obj['Routes']
	print obj['latlons']


fo.close()
