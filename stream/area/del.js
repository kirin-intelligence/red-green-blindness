$(function () {
  $(':input').labelauty()
});
var marker, map = new AMap.Map("container", {
  resizeEnable: true,
  center: [116.35716199999999, 39.971875999999995],
  zoom: 15
});
map.on('click', get_point);

var polyEditors = []
var POLYS_arr = []
var markers_start = []
var markers_end = []
var MARKERS = []
var START_MARKER = null;
var END_MARKER = null;
var MARKS_NO = null;
var DAY = null;

$('#submit').click(function () {
    choose_types = [];
    choose_day = 'evening';
    obj = document.getElementsByTagName("input");
    check_val = [];
    for (k in obj) {
      if (obj[k].checked) {
        console.log(obj[k].value);
        if (obj[k].value == 'morning') {
          choose_day = 'morning';
        }
      }
    }
    for (k in obj) {
      if (obj[k].checked) {
        choose_types.push(obj[k].value);
        // choose_type(obj[k].value, day)
      }
    }

    get_streams();

  }
);

var all_data;
$.get('area/area.php'
  , function (result) {
    all_data = eval(result);
  });

function get_streams() {
  clearMarker();
  console.log("day:" + choose_day);
  console.log("total:" + all_data.length);
  all_data.forEach(function (item, line_index) {
    var points = eval([eval(item['start_point']), eval(item['end_point'])]);
    if (choose_types.indexOf(item['type']) != -1 && item['day'] == choose_day) {
      var paths = eval(item['paths']);
      var type = (item['type']);
      var no = (item['no']);
      var distance = (item['distance']);
      var day = item['day'];
      var jam_time = parseFloat(item['jam_time']).toFixed(1);
      addMarker(points, type, no);
      // driver_match(points, type, no, distance, day)
      draw_poly(paths, type, no, distance, day, jam_time);

    }
  });
}

function addMarker(points, type, no) {
  var marker = new AMap.Marker({
    icon: "http://a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-red.png",
    position: points[0],
    offset: new AMap.Pixel(-13, -30),
    draggable: false,
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
    draggable: false,
    extData: {
      "no": no,
      'type': type,
      'is_start': false
    }
  });

  MARKERS.push(marker);
  MARKERS.push(marker_end);
  marker_end.setMap(map)


}


function draw_poly(paths, type, no, distance, jam_time) {

  var desc;
  var color;
  if (DAY) {
    if (type == "green") {
      desc = '黄色';
      color = 'yellow'
    } else if (type == "yellow") {
      desc = '橙黄';
      color = '#FF8C00'
    } else {
      desc = '红色';
      color = 'red'
    }
  } else {
    if (type == "red") {
      desc = '红色（3至6小时）'
    } else
      desc = '黄色（2小时12分钟至3小时'
  }

  var mouseHandler = function (e) {
    new AMap.InfoWindow({
      content: '<h3>序号：' + no + '</h3>' +
      '<h3>长度：' + distance + '米</h3>' +
      '<h3>拥堵程度：' + desc + '</h3>' +
      '<h3>拥堵时间：' + jam_time + '分钟</h3>',

      showShadow: true
    }).open(map, e.lnglat)

  };
  var polyline = new AMap.Polyline({
    path: paths, //设置线覆盖物路径
    strokeColor: color, //线颜色
    strokeOpacity: 1, //线透明度
    strokeWeight: 8, //线宽
    strokeStyle: "solid",
    strokeDasharray: [10, 5],
    extData: {
      "no": no,
      'type': type,
      "paths": paths,
      "distance": distance,
      "day": DAY
    }
  });

  // polyline.on('mouseover', mouseHandler);
  polyline.on('dblclick', del_line);
  polyline.setMap(map);
  POLYS_arr.push(polyline);
  var polyEditor = new AMap.PolyEditor(map, polyline);
  polyEditors.push(polyEditor);
}

function get_point(e) {
  console.log(e);
  console.log(e['lnglat']['lng'] + ',' + e['lnglat']['lat'])

}
function del_line(e) {
  var p = eval(e['target']);
  var ext = p.getExtData();
  console.log(ext);
  map.remove(p);
  map.remove(START_MARKER);
  map.remove(END_MARKER);
  START_MARKER = null;
  END_MARKER = null;
  MARKS_NO -= 1;
  $.get('area/del_path.php',
    {
      no: ext['no'],
      day: DAY,
      opera: 'del'
    }, function (result) {
      console.log(result);
    }, 'json');


}

var old_point = [];
// 清除 marker
function clearMarker() {
  map.clearMap()
}

function close_lineedit() {
  polyEditors.forEach(function (value, index) {
    value.close()
  })
}

function open_lineedit() {
  console.log(polyEditors);

  polyEditors.forEach(function (value, index) {
    value.open()
  })
}
