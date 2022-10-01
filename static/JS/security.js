
function preventBack() {
       window.history.forward();
    }
setTimeout("preventBack()", 0);
window.onunload = function () { null };


$(document).bind("contextmenu",function(e){
 alert("Right Click is Prevented");
  return false;
});

$('body').bind('cut copy paste',function(e) {
    e.preventDefault();
    alert("You are not allowed to use Cut, Copy, Paste operations");
    return false;
});

