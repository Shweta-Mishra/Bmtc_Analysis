import allpath # get the path data we previously grabbed
import sys
import random

COLORS = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#800000', '#008000', '#000080', '#808000', '#008080', '#800080']
 
fo = open('polylineJS2.js', 'w')
 
truncatedRouteList = []
 
allRoutesJavaScript = {}
for route in allpath.allroutepaths.keys():
    if route in ['1', '1E', '1F', 'CCC-1', 'FDR-1', 'G-1', 'K-1', 'KHC-1']:
        continue
    truncatedRouteList.append(route)
    routeJavaScript = []
    for path in allpath.allroutepaths[route]:
        print "inside allpath.allroute for"
        latlngJavaScript = []
        for point in path:
            print "inside second for"
            latlngJavaScript.append('%s,%s' % (point['lat'], point['lon']))
        routeJavaScript.append('[' + ','.join(latlngJavaScript) + ']')
    allRoutesJavaScript[route] = '[' + ','.join(routeJavaScript) + ']'
 
completeJS = []
for route in allRoutesJavaScript.keys(): # write up to the last one so we don't have a trailing comma
    completeJS.append('"%s": %s' % (route, allRoutesJavaScript[route]))
 
fo.write('var allData = {%s};\n' % (','.join(completeJS)))
 
# assign each route a random color
colorAssignments = []
for route in truncatedRouteList:
    colorAssignments.append('"%s": "%s"' % (route, random.choice(COLORS)))
fo.write('var routeColors = {%s};\n' % ','.join(colorAssignments))
 
fo.write('var routeNames = ["%s"];\n' % ('","'.join(truncatedRouteList)))
 
fo.write("""
for (var i = 0; i < routeNames.length; i++) { // loop over each route
   var routeName = routeNames[i];
   for (var j = 0; j < allData[routeName].length; j++) { // loop over each path on the route
       var curPath = allData[routeName][j];
       var polylinePoints = [];
       for (var k = 0; k < curPath.length; k += 2) { // loop over each point in the path
           polylinePoints.push(new google.maps.LatLng(curPath[k], curPath[k+1]));
       }
       var routePath = new google.maps.Polyline({
           path: polylinePoints,
           strokeColor: routeColors[routeName],
           strokeOpacity: 1.0,
           strokeWeight: 2
           });
       routePath.setMap(map);
   }
}
""");
 
fo.close()

