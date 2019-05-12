<?php
header("Content-Type: text/html;charset=utf-8");
$redis = new Redis();
$redis->connect('123.56.19.49', 6379); //连接Redis
$redis->auth('wscjxky123'); //密码验证
$redis->select(8);
//$keys = $redis->keys('*');
//$arr = array();
//$arr_p = array();
//foreach ($keys as $key => $value) {
//    $hdata = $redis->hGetAll($value);
//    var_dump($hdata);
//    if ((strpos($hdata['start_place'], "二环") || strpos($hdata['end_place'], "二环")))
//        continue;
//    if ((strpos($hdata['start_place'], "三环") || strpos($hdata['end_place'], "三环")))
//        continue;
//    if ((strpos($hdata['start_place'], "四环") || strpos($hdata['end_place'], "四环")))
//        continue;
//    if ((strpos($hdata['start_place'], "五环") || strpos($hdata['end_place'], "五环")))
//        continue;
//    foreach ($hdata as $k => $v) {
//        $redis->hSet("area:" . $value, $k, $v);
//    }
//}

$keys = $redis->keys('area*');
$arr = array();
$arr_p=array();
foreach ($keys as $key => $value) {
    $hset=$redis->hGetAll($value);
    array_push($arr, ($hset));
}

//file_put_contents("data_area.json", json_encode($arr));//写入
exit(json_encode($arr));
?>
