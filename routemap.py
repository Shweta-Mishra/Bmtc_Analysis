import csv
#import simplejson
with open('RouteMap.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    data = open("outputMap.csv", "w")
    lat=open("lat","w")
    w = csv.writer(data)
    #l=csv.writer(lat)
    for row in reader:
	    my_row= []
	    my_list=[]
	    latlon=[]
            #s=''
	    my_row.append("route_no:"+row[0])
            #str=s.append(row[1])
            my_list.append(row[1])
            lat.writelines(my_list)
            #simplejson.dump(my_list,lat)
            fo=open('lat','r')
            #s=str(row[1])
            #dict=eval(s);
            str=fo.read()

            dict=eval(str);
            for obj in dict:
            	latlon.append(obj['latlons'])
            my_row.append(latlon)
	    w.writerow(my_row)
