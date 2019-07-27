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

var submit_btn = $('#submit');
submit_btn.text('正在加载');// 按钮灰掉，但仍可点击。
submit_btn.prop('disabled', true);
$.get('static/data.json'
    , function (result) {
        all_data = eval(result);
        submit_btn.text('确定');
        submit_btn.prop('disabled', false);
    }, 'json');
submit_btn.click(function () {

        choose_types = [];
        choose_day = $(':radio:checked').val();
        var radioboxs = $(':checkbox:checked');
        $.each(radioboxs, function (i, obj) {
            choose_types.push($(obj).val())
        });

        get_streams();
    }
);


function get_streams() {
    clearMarker();
    all_data.forEach(function (item, line_index) {
        var points = eval([eval(item['start_point']), eval(item['end_point'])]);
        if (choose_types.indexOf(item['type']) != -1 && item['day'] == choose_day) {
            var paths = eval(item['paths']);
            var type = (item['type']);
            var no = (item['no']);
            var distance = (item['distance']);
            var day = item['day'];
            var jam_time = item['jam_time'];
            // var jam_time = ((parseFloat(item['jam_time']) * 5) / 60).toFixed(1);
            addMarker(points, type, no);
            draw_poly(paths, type, no, distance, day, jam_time);
        }
    });
}

function addMarker(points, type, no) {
    var img = 'static/images/bullet_yellow.png';
    if (type == "green") {
        img = 'static/images/bullet_yellow.png';
    } else if (type == "yellow") {
        img = 'static/images/bullet_red.png';
    } else {
        img = 'static/images/bullet_black.png';
    }
    var marker = new AMap.Marker({
        icon: img,
        position: points[0],
        offset: new AMap.Pixel(-20, -21),
        draggable: false,
        extData: {
            "no": no,
            'type': type,
            'is_start': true
        }
    });
    marker.setMap(map);
    var marker_end = new AMap.Marker({

        icon: img,
        position: points[1],
        offset: new AMap.Pixel(-20, -18),
        draggable: false,
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
    marker_end.setMap(map);

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
        var j_time = parseFloat(jam_time).toFixed(1);
        var b = j_time.split(".");
        var x = b[0];
        var y = b[1];
        var t = "<h3>拥堵时间：" + x + "小时" + (y * 6) + "分钟</h3>";

        new AMap.InfoWindow({
            content: '<h3>序号：' + no + '</h3>' +
                '<h3>长度：' + distance + '米</h3>' +
                '<h3>拥堵程度：' + desc + '</h3>' +
                t,

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
    // map.setFitView();

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

    polyEditors.forEach(function (value, index) {
        value.open()
    })
}
