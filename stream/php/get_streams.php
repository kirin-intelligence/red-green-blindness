<?php
$redis = new Redis();

$redis->connect('123.56.19.49', 6379); //连接Redis
$redis->auth('wscjxky123'); //密码验证

$day=$_GET['day'];

$redis->select(8);
//$keys = $redis->keys($day.'*');
//$arr = array();
//$arr_p=array();
//foreach ($keys as $key => $value) {
//    $hset=$redis->hGetAll($value);
//    array_push($arr, ($hset));
//    break;
//    exit(json_encode($arr));

//}

$keys = $redis->keys('evening*');
$arr = array();
$arr_p=array();
foreach ($keys as $key => $value) {
    $hset=$redis->hGetAll($value);
    array_push($arr, ($hset));
//    break;
//    exit(json_encode($arr));

}
file_put_contents("evening_data.json",json_encode($arr));//写入

$keys = $redis->keys('morning*');
$arr = array();
$arr_p=array();
foreach ($keys as $key => $value) {
    $hset=$redis->hGetAll($value);
    array_push($arr, ($hset));
//    break;
//    exit(json_encode($arr));

}
file_put_contents("morning_data.json",json_encode($arr));//写入


//header("Content-type: application/json");
//exit(json_encode($arr));




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
