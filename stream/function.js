var marker, map = new AMap.Map("container", {
  resizeEnable: true,
  center: [116.35716199999999, 39.971875999999995],
  zoom: 20
});
var polyEditors = [];
var POLYS_arr = [];
var markers_start = [];
var markers_end = [];
var MARKERS = [];
init();


function init() {

  $.get('php/get_streams.php',
    {
      'day': 'evening'
    }
    , function (result) {
      var res = eval(result);
      res.forEach(function (points, line_index) {
        points = eval(points);
        addMarker(points);
        //driver_match(points);
        driver_direct(points);
        // markers.push([marker,marker_end]);
        map.on('click', get_point);

      });
    }, 'json');

}

function addMarker(points) {
  var marker = new AMap.Marker({
    icon: "http://a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-red.png",
    position: points[0],
    offset: new AMap.Pixel(-13, -30),
    draggable: true,
    angle:1

  });

  marker.setMap(map);
  var marker_end = new AMap.Marker({
    icon: "http://a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-default.png",
    position: points[1],
    offset: new AMap.Pixel(-13, -30),
    draggable: true,
    angle:0
  });
  markers_start.push(points[0]);
  markers_end.push(points[1]);
  MARKERS.push(marker);
  MARKERS.push(marker_end);

  marker.on('dragstart', startDrag);
  marker.on('dragend', endDrag);
  marker_end.on('dragstart', startDrag);
  marker_end.on('dragend', endDrag);

  marker_end.setMap(map);


}
function startDrag(e) {
  var point = [e['lnglat']['lng']];
  var index = markers_start.indexOf(point);

  console.log(index);
}
function endDrag(e) {
  var point = [e['lng'], e['lat']];

  console.log(point);

}
function driver_direct(points) {
  draw_poly([points[1], points[0]], points[0][2], 0);

}

function driver_match(points) {
  var steps;
  var distance;
  new AMap.Driving({
    autoFitView: false,
    outlineColor: 'red',
    showTraffic: false
  }).search(points[0], points[1], function (status, result) {
    if (status === 'complete') {
      var one_steps = eval(result['routes'][0]['steps']);
      var one_distance = result['routes'][0]['distance'];
      var paths = [];
      new AMap.Driving({
        autoFitView: false,
        outlineColor: 'red',
        showTraffic: false
      }).search(points[1], points[0], function (status, result) {
        if (status === 'complete') {
          var two_steps = eval(result['routes'][0]['steps']);
          var two_distance = result['routes'][0]['distance'];
          if (parseInt(two_distance) < parseInt(one_distance)) {
            distance = two_distance;
            steps = two_steps;

          } else {
            distance = one_distance;
            steps = one_steps;
          }

          steps.forEach(function (value, index) {
            value['path'].forEach(function (locate, index) {
              paths.push([locate['R'], locate['P']]);
            });
          });


          draw_poly(paths, points[0][2], distance);

        }
      });
    }
  });
}


function draw_poly(paths, type, length) {
  var color;
  console.log(type);
  if (type === 0)
    color = "red";
  else
    color = "DarkSalmon";


  var mouseHandler = function (e) {

    new AMap.InfoWindow({
      content: '<h3>长度：' + length + '米</h3>' +
      '<h3>拥堵程度：' + type + '</h3>',
      showShadow: true
    }).open(map, e.lnglat);

  };

  var polyline = new AMap.Polyline({
    path: paths, //设置线覆盖物路径
    strokeColor: color, //线颜色
    strokeOpacity: 1, //线透明度
    strokeWeight: 8, //线宽
    strokeStyle: "solid", //线样式
    strokeDasharray: [10, 5] //补充线样式
  });

  polyline.on('mouseover', mouseHandler);
  polyline.setMap(map);
  POLYS_arr.push(polyline);
  var polyEditor = new AMap.PolyEditor(map, polyline);
  polyEditors.push(polyEditor);
}

var old_point = [];

function isEmpty(obj) {
  for (var key in obj) {
    if (obj.hasOwnProperty(key))
      return false;
  }
  return true;
}

function get_point(e) {
  //
  if (isEmpty(old_point)) {
    old_point.push([e['lnglat']['lng'], e['lnglat']['lat']]);

  } else {
    old_point.push([e['lnglat']['lng'], e['lnglat']['lat']]);
    console.log(old_point);

    addMarker(old_point);
    draw_poly(old_point, 0, 0);
    old_point = []
  }

}

// 清除 marker
function clearMarker() {
  if (marker) {
    marker.setMap(null);
    marker = null;
  }
}

function close_lineedit() {
  polyEditors.forEach(function (value, index) {
    value.close()
  })
}

function open_lineedit() {
  console.log(polyEditors)

  polyEditors.forEach(function (value, index) {
    value.open()
  })
}