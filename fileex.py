import csv
with open('busyPointsRecent.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    data = open("recentoutput.csv", "w")
    w = csv.writer(data)
    for row in reader:
	    my_row= []
	    my_row.append("{\"geometry\": {\"type\":\"LineString\",\"coordinates\":[["+row[5]+","+row[4]+"],["+row[7]+","+row[6]+"]]},\"type\":\"Feature\",\"properties\":{\"route\":\""+row[8]+"\",\"route_count\":"+row[2]+",\"trips\":"+row[3]+"}},")
	    #my_row.append(row[2])
	    #my_row.append(row[4])
	    w.writerow(my_row)

#"{\"geometry\": {\"type\"=\"LineString\",\"coordinates\":["+row[8]+","+row[10]+"]},\"type\":\"feature\",\"properties\":{\"route\":\""+row[9]+"\"}},"
