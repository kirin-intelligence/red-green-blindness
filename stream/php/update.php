<?php
error_reporting(E_ALL ^ E_NOTICE);


$redis = new Redis();

$redis->connect('123.56.19.49', 6379); //连接Redis
$redis->auth('wscjxky123'); //密码验证

$day = $_GET['day'];
$old_point1 = floatval($_GET['old_point1']);
$new_point1 = floatval($_GET['new_point1']);
$old_point2 = floatval($_GET['old_point2']);
$new_point2 = floatval($_GET['new_point2']);
$old_point = [$old_point1, $old_point2];
$new_point = [$new_point1, $new_point2];

$redis->select(5);
$keys = $redis->keys($day . ':*');
$arr = array();
$arr_p = array();

//$redis->lSet()
foreach ($keys as $first => $key) {
    $points = $redis->lRange($key, 0, -1);
    foreach ($points as $second => $value2) {
        $value2 = (json_decode($value2));

        if (abs($value2[0][0] - $old_point[0])<0.000001 and abs($value2[0][1] - $old_point[1])<0.000001 ){
            array_push($new_point, $value2[0][2]);
            array_push($arr, $new_point);
            array_push($arr, $value2[1]);
            $result = $redis->lSet($key, $second, json_encode($arr));
        }
        else if (abs($value2[1][0] - $old_point[0])<0.000001 and abs($value2[1][1] - $old_point[1])<0.000001) {
            array_push($new_point, $value2[1][2]);
            array_push($arr, $new_point);
            array_unshift($arr, $value2[0]);

            $result = $redis->lSet($key, $second, json_encode($arr));

        }

    }
}
exit(json_encode($result));


// 使用给定的用户定义函数对数组排序
function compareByTimeStamp($time1, $time2)
{
    if (strtotime($time1) < strtotime($time2))
        return -1;
    else if (strtotime($time1) > strtotime($time2))
        return 1;
    else
        return 0;
}


?>