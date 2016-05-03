var allData = {};
var routeColors = {};
var routeNames = [""];

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
