var marker, map = new AMap.Map("container", {
    resizeEnable: true,
    center: [116.35716199999999, 39.971875999999995],
    zoom: 15
});
map.on('click', get_point);

var polyEditors = [];
var POLYS_arr = [];
var markers_start = [];
var markers_end = [];
var MARKERS = [];
/*init('morning');
init('evening');*/
init('json');



function init(day) {
    $.get('php/get_streams.php',
        {
            day: day
        }
        , function (result) {
            var res = eval(result);
            console.log("total:" + result.length);
            res.forEach(function (item, line_index) {
                console.log(line_index);
                var points = eval([eval(item['start_point']), eval(item['end_point'])]);
                var paths = eval(item['paths']);
                var type = (item['type']);
                var no = (item['no']);
                var distance = (item['distance']);
                var day = item['day'];
                var jam_time = item['jam_time'];
                // driver_match(points, type, no, distance, day, jam_time)
            })
        }, 'json');


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
        }, 'json');
}

function driver_match(points, type, no, m_distance, day, jam_time) {
    var steps;
    var driving_1 = new AMap.Driving({
        policy: AMap.DrivingPolicy.LEAST_DISTANCE,
        autoFitView: false,
        outlineColor: 'red',
        showTraffic: false
    }).search(points[0], points[1], function (status, result) {
        if (status === 'complete') {
            var one_steps = eval(result['routes'][0]['steps']);
            var one_m_distance = result['routes'][0]['distance'];
            var paths = [];
            var driving_2 = new AMap.Driving({
                policy: AMap.DrivingPolicy.LEAST_DISTANCE,
                autoFitView: false,
                outlineColor: 'red',
                showTraffic: false
            }).search(points[1], points[0], function (status, result) {
                if (status === 'complete') {
                    var two_steps = eval(result['routes'][0]['steps']);
                    var two_m_distance = result['routes'][0]['distance'];
                    if (parseInt(two_m_distance) < parseInt(one_m_distance)) {
                        m_distance = two_m_distance;
                        steps = two_steps;
                    } else {
                        m_distance = one_m_distance;
                        steps = one_steps;
                    }
                    if (parseInt(m_distance) > 1000) {
                        var m_distance = Math.round(AMap.GeometryUtil.distance(points[0], points[1]));
                        console.log(m_distance);
                        update_data(points, points, type, no, m_distance, day);
                        draw_poly(points, type, no, m_distance, day, jam_time);
                        return
                    }
                    steps.forEach(function (value, index) {
                        value['path'].forEach(function (locate, index) {
                            paths.push([locate['lng'], locate['lat']])
                        })
                    });
                    update_data(points, paths, type, no, m_distance, day);
                    draw_poly(paths, type, no, m_distance, day, jam_time);
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
            desc = '黄色（3小时到5小时）'
            color = 'yellow'
        } else if (type == "yellow") {
            desc = '橙黄（5小时到8小时）'
            color = '#FF8C00'
        } else {
            desc = '红色（8小时到10小时）'
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
            "day": day
        }
    })

    polyline.on('mouseover', mouseHandler)
    polyline.setMap(map)
    POLYS_arr.push(polyline)
    var polyEditor = new AMap.PolyEditor(map, polyline)
    polyEditors.push(polyEditor)
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

