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
var choose_day ;
var choose_types;


$('#submit').click(function () {
        choose_types=[];
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


function get_streams() {
    clearMarker();
    $('button').text('正在加载');// 按钮灰掉，但仍可点击。
    $('button').prop('disabled', true);
    $.get('php/' + choose_day + '_data.json'
        , function (result) {
            var res = eval(result);
            console.log("day:" + choose_day);
            console.log("total:" + result.length);
            res.forEach(function (item, line_index) {
                var points = eval([eval(item['start_point']), eval(item['end_point'])]);
                if (choose_types.indexOf(item['type'])!=-1) {
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
            $('button').text('确定');
            $('button').prop('disabled', false)


        }, 'json')


    // draw_poly(paths, type, no, distance, day);
    // markers.push([marker,marker_end]);
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
    marker.on('dragstart', startDrag)
    marker.on('dragend', endDrag)
    marker_end.on('dragstart', startDrag)
    marker_end.on('dragend', endDrag)
    marker_end.setMap(map)


}

var old_point

function startDrag(e) {
    old_point = [e['target']['D']['position']['R'], e['target']['D']['position']['P']]


    // var index = markers_start.indexOf(point);
}

function endDrag(e) {
    console.log(e)
    var point = [e['lnglat']['R'], e['lnglat']['P']]
    console.log(point, old_point)
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
                alert(result)
            }
        }, 'json')

}

function driver_direct(paths, type, no, distance) {
    draw_poly(paths, type, no, distance)

}

function update_data(points, paths, type, no, distance, day) {
    $.get('php/upload_path.php',
        {
            points: JSON.stringify(points),
            paths: JSON.stringify(paths),
            type: type,
            no: no,
            distance: distance,
            day: day
        }, function (result) {
            console.log(result);
        }, 'json');
}

function driver_match(points, type, no, distance, day) {
    var steps;
    var driving_1 = new AMap.Driving({
        policy: AMap.DrivingPolicy.LEAST_DISTANCE,
        autoFitView: false,
        outlineColor: 'red',
        showTraffic: false
    }).search(points[0], points[1], function (status, result) {
        if (status === 'complete') {
            var one_steps = eval(result['routes'][0]['steps'])
            var one_distance = result['routes'][0]['distance']
            var paths = []
            var driving_2 = new AMap.Driving({
                policy: AMap.DrivingPolicy.LEAST_DISTANCE,
                autoFitView: false,
                outlineColor: 'red',
                showTraffic: false
            }).search(points[1], points[0], function (status, result) {
                if (status === 'complete') {
                    console.log(result['routes']);
                    var two_steps = eval(result['routes'][0]['steps'])
                    var two_distance = result['routes'][0]['distance']
                    console.log(two_distance);

                    if (parseInt(two_distance) < parseInt(one_distance)) {
                        distance = two_distance;
                        steps = two_steps;
                    } else {
                        distance = one_distance;
                        steps = one_steps;
                    }
                    if (parseInt(distance) > 1000) {
                        if (parseInt(distance) > 1500) {
                            distance = '879'
                        }
                        update_data(points, points, type, no, distance, day);
                        // draw_poly(points, type, no, distance, day)
                        return
                    }
                    steps.forEach(function (value, index) {
                        value['path'].forEach(function (locate, index) {
                            paths.push([locate['lng'], locate['lat']])
                        })
                    })
                    update_data(points, paths, type, no, distance, day);
                    // draw_poly(paths, type, no, distance, day)
                }
            })
        }
    })
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
    })

    polyline.on('mouseover', mouseHandler)
    polyline.setMap(map)
    POLYS_arr.push(polyline)
    var polyEditor = new AMap.PolyEditor(map, polyline)
    polyEditors.push(polyEditor)
}

var old_point = []

function isEmpty(obj) {
    for (var key in obj) {
        if (obj.hasOwnProperty(key))
            return false
    }
    return true
}

function get_point(e) {
    //
    // if (isEmpty(old_point)) {
    //     old_point.push([e['lnglat']['lng'], e['lnglat']['lat']]);
    //
    // } else {
    //     old_point.push([e['lnglat']['lng'], e['lnglat']['lat']]);
    //
    //
    //     addMarker(old_point);
    //     draw_poly(old_point, 0, 0);
    //     old_point = []
    // }
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

// 116.355896,39.929737  116.356218,39.922332
// 116.356229,39.922184  116.356593,39.91407
// 116.356593,39.913976  116.356406,39.909688
// 116.356395,39.908544  116.356443,39.9074
// 116.356481,39.910577 116.355789,39.907972
// 116.355692,39.931699  116.355762,39.929737
// 116.355767,39.929338  116.355832,39.927536
// 116.355842,39.92738  116.355955,39.92464
// 116.356046,39.922727  116.356234,39.918703
// 116.35654,39.911869  116.356288,39.910256
// 116.356497,39.908754  116.35676,39.913223
