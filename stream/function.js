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
      'day': 'morning'
    }
    , function (result) {
      var res = eval(result);
      res.forEach(function (item, line_index) {
        // console.log(item);
        var points = eval([eval(item['start_point']), eval(item['end_point'])]);
        var paths = item['paths'];

        var type = (item['type']);
        var no = (item['no']);
        var distance = (item['distance']);
        var day = (item['day']);
        console.log(paths);
        // console.log(points, type, no,paths);
        addMarker(points, type, no);
        driver_match(points,type, no, distance, day);
        // draw_poly(paths, type, no, distance, day);
        // markers.push([marker,marker_end]);
        map.on('click', get_point);

      });
    }, 'json');

}

function addMarker(points, type, no) {
  var marker = new AMap.Marker({
    icon: "http://a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-red.png",
    position: points[0],
    offset: new AMap.Pixel(-13, -30),
    draggable: true,
    extData: {
      "no": no,
      'type': type,
      'is_start': true
    }
  });

  marker.setMap(map);
  var marker_end = new AMap.Marker({
    icon: "http://a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-default.png",
    position: points[1],
    offset: new AMap.Pixel(-13, -30),
    draggable: true,
    extData: {
      "no": no,
      'type': type,
      'is_start': false
    }
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
var old_point;
function startDrag(e) {
  old_point = [e['target']['D']['position']['R'], e['target']['D']['position']['P']];
  console.log(old_point);

  // var index = markers_start.indexOf(point);
}
function endDrag(e) {
  console.log(e);
  var point = [e['lnglat']['R'], e['lnglat']['P']];
  console.log(point, old_point);
  $.get('php/update.php',
    {
      'day': 'evening',
      'old_point1': old_point[0],
      'old_point2': old_point[1],
      'new_point1': point[0],
      'new_point2': point[1]
    }
    , function (result) {
      if ((result)) {
        // draw_poly([point,old_point],0,0);
        alert(result);
      }
    }, 'json');

}
function driver_direct(paths, type, no, distance) {
  draw_poly(paths, type, no, distance);

}

function driver_match(points, type, no, distance, day) {
  var steps;
  var driving_1=new AMap.Driving({
    policy:AMap.DrivingPolicy.LEAST_DISTANCE,
    autoFitView: false,
    outlineColor: 'red',
    showTraffic: false
  }).search(points[0], points[1], function (status, result) {
    if (status === 'complete') {
      var one_steps = eval(result['routes'][0]['steps']);
      var one_distance = result['routes'][0]['distance'];
      var paths = [];
      var driving_2=new AMap.Driving({
        policy:AMap.DrivingPolicy.LEAST_DISTANCE,
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
          if (parseInt(distance)>1800){
            draw_poly();
            draw_poly(points, type, no, distance, day);
            return;
          }
          steps.forEach(function (value, index) {
            console.log(steps);
            value['path'].forEach(function (locate, index) {
              paths.push([locate['R'], locate['P']]);
            });
          });
          draw_poly(paths, type, no, distance,day);
        }
      });
    }
  });
}


function draw_poly(paths, type, no, distance, day) {
  var desc;
  if (day) {
    if (type == "red") {
      desc = '红色（1.5小时至3小时）';
    }
    else
      desc = '黄色（1小时6分钟至1.5小时';
  }
  else {
    if (type == "red") {
      desc = '红色（3至6小时）';
    }
    else
      desc = '黄色（2小时12分钟至3小时';
  }

  var mouseHandler = function (e) {
    new AMap.InfoWindow({
      content: '<h3>长度：' + distance + '米</h3>' +
      '<h3>拥堵程度：' + desc + '</h3>',
      showShadow: true
    }).open(map, e.lnglat);

  };
  var polyline = new AMap.Polyline({
    path: paths, //设置线覆盖物路径
    strokeColor: type, //线颜色
    strokeOpacity: 1, //线透明度
    strokeWeight: 8, //线宽
    strokeStyle: "solid",
    strokeDasharray: [10, 5],
    extData: {
      "no": no,
      'type': type,
      "paths": paths,
      "distance": distance,
      "day": day
    }
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