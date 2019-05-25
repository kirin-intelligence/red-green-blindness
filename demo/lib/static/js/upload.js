function add_image(value, row, index) {
  var no = row['no'];
  var day = row['day'];
  var result = "";
  result += '<button class="btn btn-default" no="' + no + '"  day="' + day + '" onclick="upload_image(this)">上传</button>';

  result += '<button class="btn btn-default"  day="' + day + '"  no="' + no + '" onclick="prev_image(this)">查看</button>';


  return result;
}
function upload_image(obj) {
  $("#doc-modal-1").modal();
  $('#up-btn-ok').attr('no', $(obj).attr('no')).attr('day', $(obj).attr('day'));

}
function prev_image(obj) {
  $("#doc-modal-2").children('div').children('ul').html();
  //noinspection JSDuplicatedDeclaration
  $.ajax({
    url: 'php/get_imgs.php',
    type: 'GET',
    data: {
      'no': $(obj).attr('no'),
      'day': $(obj).attr('day')
    },
    dataType: "json",
    success: function (result) {
      // var imgs = JSON.parse(result);
      console.log(result);
      result.forEach(function (value, index) {
        var place = value.split("_")[3];
        console.log($("#doc-modal-2").children('div').children('ul'));
        console.log(value.split("_"));
        value="'"+value+"'";
        $("#doc-modal-2").children('div').children('ul').append(
          '<p onclick="show_img('+value+')">地理位置：' + place + '</p>'
        )
      });
      $("#doc-modal-2").modal();
    },
  });
}
function show_img(img_src) {
  var width = window.screen.availWidth;
  var height = window.screen.availHeight;
  $("#doc-modal-3").children('img').attr("width", width * 0.5).attr("height", height / 3).attr('src',img_src);
  $("#doc-modal-3").modal();

}
var position = {
  lat: 116.339073,
  lng: 39.948693,
  place: "西二环路辅路"
};

function getObjectURL(file) {
  var url = null;
  if (window.createObjectURL != undefined) { // basic
    url = window.createObjectURL(file);
  } else if (window.URL != undefined) { // mozilla(firefox)
    url = window.URL.createObjectURL(file);
  } else if (window.webkitURL != undefined) { // webkit or chrome
    url = window.webkitURL.createObjectURL(file);
  }
  return url;
}

function submit_image(obj) {
  console.log($(obj).attr('no'));
  var fileName = file.name;
  var fileType = fileName.type;
  var formData = new FormData();
  formData.append("file", file);
  formData.append("no", $(obj).attr('no'));
  formData.append("day", $(obj).attr('day'));
  formData.append("lat", position['lat']);
  formData.append("lng", position['lng']);
  formData.append("place", position['place']);
  $.ajax({
    url: 'php/upload_img.php',
    type: 'POST',
    cache: false,
    data: formData,
    processData: false,
    contentType: false,
    dataType: "json",
    success: function (result) {
      console.log(result);
      //上传成功的处理
      $("#doc-modal-1").modal('close');
      alert('上传成功');
      $("#image").attr("src", "");
      file = null;

    },
  });
}

var file;
$('#inputImage').on('change', function () {
  file = this.files[0];
  var width = window.screen.availWidth;
  var height = window.screen.availHeight;
  var objUrl = getObjectURL(file); //获取图片的路径，该路径不是图片在本地的路径
  if (objUrl) {
    $("#image").attr("width", width * 0.5).attr("height", height / 3).attr("src", objUrl);
    $('#location').text('位置: ' + position['lat'] + ',' + position['lng']);
    if (position['place'])
      $('#angle').text('地点: ' + position['place']);
  }
});


var geolocation = new AMap.Geolocation({
  // 是否使用高精度定位，默认：true
  enableHighAccuracy: true,
  // 设置定位超时时间，默认：无穷大
  timeout: 5000,
  //  定位成功后调整地图视野范围使定位位置及精度范围视野内可见，默认：false
  zoomToAccuracy: true,

})

geolocation.getCurrentPosition();
AMap.event.addListener(geolocation, 'complete', onComplete);
AMap.event.addListener(geolocation, 'error', onError);

function onComplete(data) {
  // data是具体的定位信息
  position = data['position'];
  console.log(position);
  var geocoder = new AMap.Geocoder({});
  // [position['lat'], position['lng']]
  geocoder.getAddress([position['lat'], position['lng']], function (status, result) {
    if (status === 'complete' && result.info === 'OK') {
      position['place'] = result;
      console.log(position)
    }
    else {
      position = {
        lat: 116.339073,
        lng: 39.948693,
        place: "西二环路辅路"
      };
      console.log(status)

    }
  });

}

function onError(data) {
  // 定位出错
  position = {
    lat: 116.339073,
    lng: 39.948693,
    place: "西二环路辅路"
  };
  console.log(position);
}
// var geolocation = new $.AMUI.Geolocation();
// geolocation.get({timeout: 7000}).then(function(position) {
//   console.log(position.coords);
//   var contentString = '纬度 ' + position.coords.latitude +
//     '，经度 ' + position.coords.longitude;
//   return contentString;
// });

