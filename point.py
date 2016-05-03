import csv
with open('latlon.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    data = open("Pointoutput.csv", "w")
    w = csv.writer(data)
    for row in reader:
	    my_row= []
	    my_row.append("{\"geometry\": {\"type\":\"Point\",\"coordinates\":["+row[1]+","+row[0]+"]},\"type\":\"Feature\",\"properties\":{}},")
	    #my_row.append(row[2])
	    #my_row.append(row[4])
	    w.writerow(my_row)

#"{\"geometry\": {\"type\"=\"LineString\",\"coordinates\":["+row[8]+","+row[10]+"]},\"type\":\"feature\",\"properties\":{\"route\":\""+row[9]+"\"}},"
