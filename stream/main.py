# from report import *
# from RGB_color import *
# from split_dir import *
import json

def write_html(gps_center, result):
    html = '''
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
    <title>默认点标记</title>
    <link rel="stylesheet" href="https://a.amap.com/jsapi_demos/static/demo-center/css/demo-center.css"/>
    <style>
        html,
        body,
        #container {
            width: 100%%;
            height: 100%%;
        }

        .amap-icon img,
        .amap-marker-content img {
            width: 25px;
            height: 34px;
        }

        .marker {
            position: absolute;
            top: -20px;
            right: -118px;
            color: #fff;
            padding: 4px 10px;
            box-shadow: 1px 1px 1px rgba(10, 10, 10, .2);
            white-space: nowrap;
            font-size: 12px;
            font-family: "";
            background-color: #25A5F7;
            border-radius: 3px;
        }

        .input-card {
            width: 32rem;
            z-index: 170;
        }

        .input-card .btn {
            margin-right: .8rem;
        }

        .input-card .btn:last-child {
            margin-right: 0;
        }
    </style>
</head>
<body>
<div id="container"></div>
<div class="input-card">
    <label style="color:grey">点标记操作</label>
    <div class="input-item">
        <input id="addMarker" type="button" class="btn" onclick="open_lineedit()" value="编辑线段">
                <input id="addMarker" type="button" class="btn" onclick="close_lineedit()" value="取消编辑">

    </div>
</div>
<script type="text/javascript"
        src="https://webapi.amap.com/maps?v=1.4.13&key=2be4c36d53e74e0c585326d62d6fe6e3"></script>
<script type="text/javascript"
        src='https://webapi.amap.com/maps?v=1.4.13&key=c536f4eae991666b64267ca01f855153&plugin=AMap.Driving'></script>
<script src="https://webapi.amap.com/maps?v=1.4.13&key=c536f4eae991666b64267ca01f855153&plugin=AMap.PolyEditor"></script>
<script type="text/javascript">
   
</script>
</body>
</html>''' % (gps_center, result)

    with open('test.html', 'w')as f:
        f.write(html)
    os.system('google-chrome-stable /home/kirin/Python_Code/red-green-blindness/stream/test.html')


from redis import StrictRedis, ConnectionPool
pool = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=5)
redis = StrictRedis(connection_pool=pool)
if __name__ == '__main__':
    day = 'evening'
#    # 西直门
#    # gps_center = [116.35716199999999,39.971875999999995]
    gps_center = [116.35716199999999, 39.971875999999995]
#    # 紫竹桥
#    gps_center = [116.30756199999999, 39.944875999999994]
#    input_dir = '/run/media/kirin/新加卷/server/'
#    target_dir = '/run/media/kirin/新加卷1/images/'
#    # spilt_file(input_dir,target_dir)
#    print(day)
#    rgb_img = run_rgb(target_dir, day, gps_center)
#    result = report(rgb_img, gps_center)
#    print(result)
#    img = cv2.imread("out_put.png")
#    write_html(gps_center, result)
#    cv2.imshow('a', img)
#    cv2.waitKey(0)
    redis_key="%s:%s_%s"%(day,gps_center[0],gps_center[1])
    results= [[[116.35431943944634, 39.9765566569343, 0], [116.35443743252593, 39.97489789781021, 0]], [[116.35124089273354, 39.97656486861313, 0], [116.3531073287197, 39.97656486861313, 0]], [[116.36234296885812, 39.97658950364963, 0], [116.36358725951555, 39.97658950364963, 0]], [[116.3601654602076, 39.97650738686131, 0], [116.361677916955, 39.97650738686131, 0]], [[116.36169937024219, 39.9765320218978, 0], [116.36230006228372, 39.97650738686131, 0]], [[116.35072601384081, 39.97646632846715, 0], [116.35332186159168, 39.97646632846715, 0]], [[116.35429798615915, 39.974298445255464, 0], [116.35439452595153, 39.974799357664224, 0]], [[116.35425507958476, 39.97413421167882, 0], [116.35453397231832, 39.97006943065693, 0]], [[116.35266753633216, 39.96804935766423, 0], [116.35297860899652, 39.96867344525547, 0]], [[116.35497376470586, 39.96859132846715, 0], [116.35587480276814, 39.968238226277364, 0]], [[116.35134815916953, 39.967786583941596, 0], [116.36201044290655, 39.967786583941596, 0]], [[116.35346130795845, 39.967663408759115, 0], [116.35599279584774, 39.967663408759115, 0]], [[116.35673293425604, 39.967663408759115, 0], [116.3585457370242, 39.967663408759115, 0]], [[116.35072601384081, 39.967663408759115, 0], [116.35343985467127, 39.967663408759115, 0]], [[116.36275058131486, 39.9675566569343, 0], [116.36358725951555, 39.9675566569343, 0]], [[116.35420144636676, 39.975300270072985, 1], [116.35428725951556, 39.97415884671532, 1]], [[116.35295715570932, 39.96871450364963, 1], [116.3531716885813, 39.969231839416054, 1]]]
    for i in results:
        redis.sadd(redis_key,json.dumps(i))
        
