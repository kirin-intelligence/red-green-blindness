<?php
$redis = new Redis();

$redis->connect('123.56.19.49', 6379,); //连接Redis
$redis->auth('wscjxky123'); //密码验证

$day=$_GET['day'];

$redis->select(5);
$keys = $redis->keys($day.':*');
$arr = array();

foreach ($keys as $key => $value) {
    $points=$redis->sGetMembers($value);
    exit(json_encode($points));

    array_push($arr,json_decode($points));
}
exit(json_encode($arr));




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