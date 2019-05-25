function isMobile() {
  var userAgentInfo = navigator.userAgent;

  var mobileAgents = ["Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod"];

  var mobile_flag = false;

  //根据userAgent判断是否是手机
  for (var v = 0; v < mobileAgents.length; v++) {
    if (userAgentInfo.indexOf(mobileAgents[v]) > 0) {
      mobile_flag = true;
      break;
    }
  }

  var screen_width = window.screen.width;
  var screen_height = window.screen.height;

  //根据屏幕分辨率判断是否是手机
  if (screen_width < 500 && screen_height < 800) {
    mobile_flag = true;
  }

  return mobile_flag;
}
$(document).ready(function () {
  $.goup({
    trigger: 110,
    bottomOffset: 80,
    locationOffset: 80,
    title: '回到顶部',
    titleAsText: true,
    containerSize: 400
  });
});
$(function () {
  var src_posi_Y = 0, dest_posi_Y = 0, move_Y = 0, is_mouse_down = false, destHeight = 30;
  $("#expander")
    .mousedown(function (e) {
      src_posi_Y = e.pageY;//鼠标指针的位置
      is_mouse_down = true;
    });
  $(document).bind("click mouseup", function (e) {
    if (is_mouse_down) {
      is_mouse_down = false;
    }
  })
    .mousemove(function (e) {
      dest_posi_Y = e.pageY;
      move_Y = src_posi_Y - dest_posi_Y;
      src_posi_Y = dest_posi_Y;
      destHeight = $("#main-contain").height() - move_Y;
      if (is_mouse_down) {
        $("#main-contain").css("height", destHeight > 30 ? destHeight : 30);
      }
    });
});
