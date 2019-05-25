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

$day = $_GET['day'];
$no = $_GET['no'];
$hname = 'area:' . $day . ':' . $no;
$res = $redis->del($hname);
exit(1);



