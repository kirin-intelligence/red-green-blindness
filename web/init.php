<?php
$redis = new Redis();

$redis->connect('123.56.19.49', 6379); //连接Redis
$redis->auth('wscjxky123'); //密码验证

$redis->select(1);
$keys = $redis->keys('gaode:*');
$arr=array();
foreach ($keys as $key=>$value){
    $time=substr($value,strlen('gaode:'),strlen('2019-03-02-10_55_23'));
//    $points= $redis->hGet($value,"points");//输出value
    array_push($arr,$time);

}
exit(json_encode($arr));
?>