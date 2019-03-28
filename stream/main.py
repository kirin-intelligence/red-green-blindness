from report import *
from RGB_color import *
from split_dir import *


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


if __name__ == '__main__':
    day = 'evening'
    # 西直门
    # gps_center = [116.35716199999999,39.971875999999995]
    gps_center = [116.35716199999999, 39.971875999999995]
    # 紫竹桥
    gps_center = [116.30756199999999, 39.944875999999994]
    input_dir = '/run/media/kirin/新加卷/server/'
    target_dir = '/run/media/kirin/新加卷1/images/'
    # spilt_file(input_dir,target_dir)
    print(day)
    rgb_img = run_rgb(target_dir, day, gps_center)
    result = report(rgb_img, gps_center)
    print(result)
    img = cv2.imread("out_put.png")
    write_html(gps_center, result)
    cv2.imshow('a', img)
    cv2.waitKey(0)
