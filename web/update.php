<?php
$redis = new Redis();

$redis->connect('123.56.19.49', 6379); //连接Redis
$redis->auth('wscjxky123'); //密码验证

$redis->select(2);
$keys = $redis->keys('gaode:*');
$time=$_GET['time'];

$time=substr_replace($time,'-',strlen('2019-03-02'),1);
$time=strtr($time,':','_');
foreach ( $keys as $key=>$value){
    exit(($redis->hGet('gaode:'.$time,"points")));//输出value
}
?>