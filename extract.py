#!/usr/bin/python

LatLonslist=[]
fo = open("route", "r")

#for reading
str=fo.read()

dict=eval(str);

for obj in dict:
	#print obj['latlons'][0], " ", obj['latlons'][1]
	#list.append(obj['latlons'])
	LatLonObject={'lat':obj['latlons'][0],'lon':obj['latlons'][1]}
	LatLonslist.append(LatLonObject)	

print LatLonslist

fo.close()
