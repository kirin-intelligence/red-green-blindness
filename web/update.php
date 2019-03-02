<?php
$redis = new Redis();

$redis->connect('123.56.19.49', 6379); //连接Redis
$redis->auth('wscjxky123'); //密码验证

$redis->select(1);
$keys = $redis->keys('gaode:*');
$time=$_GET['time'];
foreach ( $keys as $key=>$value){
    exit(($redis->hGet('gaode:'.$time,"points")));//输出value
}
?>