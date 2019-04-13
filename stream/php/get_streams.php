<?php
$redis = new Redis();
$redis->connect('123.56.19.49', 6379); //连接Redis
$redis->auth('wscjxky123'); //密码验证
$redis->select(8);
$keys = $redis->keys('*');
$arr = array();
$arr_p=array();
foreach ($keys as $key => $value) {
    $hset=$redis->hGetAll($value);
    array_push($arr, ($hset));
}

file_put_contents("data.json",json_encode($arr));//写入
exit(json_encode(1));
?>
