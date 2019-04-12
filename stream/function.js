$(function () {
  $(':input').labelauty()
})
var marker, map = new AMap.Map("container", {
  resizeEnable: true,
  center: [116.35716199999999, 39.971875999999995],
  zoom: 15
})
map.on('click', get_point)

var polyEditors = []
var POLYS_arr = []
var markers_start = []
var markers_end = []
var MARKERS = []
var all_data = []
var yellow_data = []
var red_data = []
var green_data = []
var choose_day;
var choose_types;


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

$('button').text('正在加载');// 按钮灰掉，但仍可点击。
$('button').prop('disabled', true);
$.get('php/data.json'
  , function (result) {
    all_data = eval(result);
    $('button').text('确定');
    $('button').prop('disabled', false);
  }, 'json');

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
  })

  marker.setMap(map)
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
  })

  markers_start.push(points[0])
  markers_end.push(points[1])
  MARKERS.push(marker)
  MARKERS.push(marker_end)
  marker_end.setMap(map)

}

function draw_poly(paths, type, no, distance, day, jam_time) {
  var desc;
  var color;
  if (day) {
    if (type == "green") {
      desc = '黄色';
      color = 'yellow'
    } else if (type == "yellow") {
      desc = '红色';
      color = 'red'
    } else {
      desc = '深红';
      color = '#660000'
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

  }
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
      "day": day
    }
  });
  map.setFitView();

  polyline.on('dblclick', poly_dblclick);
  polyline.on('mouseover', mouseHandler);
  polyline.setMap(map)
  POLYS_arr.push(polyline);
  var polyEditor = new AMap.PolyEditor(map, polyline)
  polyEditors.push(polyEditor)
}
function poly_dblclick(e) {
  var no = e.target.getExtData()['no'];
  var t = $('#table').offset().top;//  获取需要跳转到标签的top值
  $(window).scrollTop(t);
  search(no);

}

function get_point(e) {
  console.log(e)
  console.log(e['lnglat']['lng'] + ',' + e['lnglat']['lat'])


}

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
  console.log(polyEditors)

  polyEditors.forEach(function (value, index) {
    value.open()
  })
}
