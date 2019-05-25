<?php
header('Access-Control-Allow-Origin: *');   // 解决前段javascript跨域请求
header("content-type:text/html;charset=utf8");

//print_r($_FILES);
$time=rand(0,100);
$uniqid = md5(uniqid(microtime(true),true));
$lat= $_POST['lat'];
$day= $_POST['day'];
$lng = $_POST['lng'];
$no =$_POST['no'];
$place =$_POST['place'];
$tmp_name = $_FILES['file']['tmp_name'];
$tmp_type = 'jpg';
$dirname='data/'.$day.'_'.$no;
$place=characet($place);
if(!is_dir($dirname)){
    mkdir(iconv("UTF-8", "GBK", $dirname),0777,true);
}
$filename = $dirname.'/'.$lng."_".$lat.'_'.$time.'.jpg';

//将服务器上的临时文件移动到指定目录下
//使用该方法move_uploaded_file($tmp_name , $destination)

move_uploaded_file($tmp_name , $filename);
function characet($data){
    if( !empty($data) ){
        $fileType = mb_detect_encoding($data , array('UTF-8','GBK','LATIN1','BIG5')) ;
        if( $fileType != 'UTF-8'){
            $data = mb_convert_encoding($data ,'utf-8' , $fileType);
        }
    }
    return $data;
}
exit(json_encode($filename));