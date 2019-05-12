<?php

$no = $_GET['no'];
$day = $_GET['day'];
$dirname='data/'.$day.'_'.$no;
$files = walk($dirname);
exit (json_encode($files));

function walk($path)
{
    //判断目录是否为空
    if (!file_exists($path)) {
        return array();
    }

    $fileItem = array();

    //切换如当前目录
    chdir($path);

    foreach (glob('*') as $v) {
        $newPath = $path . DIRECTORY_SEPARATOR . $v;
        array_push($fileItem,'php/'.characet($newPath));
    }
    return $fileItem;
}

function characet($data){
    if( !empty($data) ){
        $fileType = mb_detect_encoding($data , array('UTF-8','GBK','LATIN1','BIG5')) ;
        if( $fileType != 'UTF-8'){
            $data = mb_convert_encoding($data ,'utf-8' , $fileType);
        }
    }
    return $data;
}