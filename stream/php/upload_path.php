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

$day = $_GET['day'];
$paths = $_GET['paths'];
$type = $_GET['type'];
$no = $_GET['no'];
$distance = $_GET['distance'];
$day = $_GET['points'];

$redis->select(8);
$hname=$day.':'.$no;
//$res=$redis->hGet($hname,'paths');
$res=$redis->hSet($hname,'paths',$paths);
$res=$redis->hSet($hname,'distance',$distance);

var_dump($res);


