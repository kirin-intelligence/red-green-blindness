<?php
$redis = new Redis();

$redis->connect('123.56.19.49', 6379); //连接Redis
$redis->auth('wscjxky123'); //密码验证

$redis->select(1);
$keys = $redis->keys('gaode:*');
$arr = array();
foreach ($keys as $key => $value) {
    $time = substr($value, strlen('gaode:'), strlen('2019-03-02-10_55_23'));
//    $points= $redis->hGet($value,"points");//输出value
    $time=substr_replace($time,' ',strlen('2019-03-02'),1);
    $time=strtr($time,'_',':');
    array_push($arr, $time);

}

usort($arr, "compareByTimeStamp");
//var_dump( $arr);

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