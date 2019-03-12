<?php
$redis = new Redis();

$redis->connect('123.56.19.49', 6379); //连接Redis
$redis->auth('wscjxky123'); //密码验证

$page=$_GET['page'];

$redis->select(2);
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

$each_len=70;
$pages=ceil(count($arr)/$each_len);
if ($page>=$pages)
	$page=$pages-1;
if ($page<=0)
	$page=0;
$arr=array_slice($arr,$each_len*$page,$each_len);
array_unshift($arr,$page);

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