var map = L.map('leaflet', {
  'center': [0, 0],
  'zoom': 0,
  'layers': [
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      'attribution': 'Map data &copy; OpenStreetMap contributors'
    })
  ]
});

var polyline = new L.Polyline([
  [-45, 45],
  [45, -45]
], {
  color: 'green',
  weight: 5,
  opacity: 0.5
}).addTo(map);

map.fitBounds(polyline.getBounds());
