<?php
/**
 * Created by PhpStorm.
 * User: xky
 * Date: 2019/4/9
 * Time: 6:27 PM
 */
error_reporting(E_ALL ^ E_NOTICE);

//points, paths, type, no, distance, day
$redis = new Redis();

$redis->connect('123.56.19.49', 6379); //连接Redis
$redis->auth('wscjxky123'); //密码验证
$redis->select(10);

$opera = $_GET['opera'];
$day = $_GET['day'];
$no = $_GET['no'];
$hname = $day . ':' . $no;
if ($opera == 'del') {
    $res = $redis->del($hname);
    exit(1);
}
$paths = $_GET['paths'];
$type = $_GET['type'];
$distance = $_GET['distance'];


//$res=$redis->hGet($hname,'paths');
$res = $redis->hSet($hname, 'day', $day);
$res = $redis->hSet($hname, 'type', $type);
$res = $redis->hSet($hname, 'no', $no);
$res = $redis->hSet($hname, 'distance', $distance);
$res = $redis->hSet($hname, 'paths', $paths);
exit(1);




