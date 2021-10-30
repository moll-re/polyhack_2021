var currentscrollHeight = 0;
var count = 0;
jQuery(document).ready(function ($) {
    for (var i = 0; i < 8; i++) {
        callData(count);//Call 8 times on page load
        count++;
    }
});
$(window).on("scroll", function () {
    const scrollHeight = $(document).height();
    const scrollPos = Math.floor($(window).height() + $(window).scrollTop());
    const isBottom = scrollHeight - 100 < scrollPos;
    if (isBottom && currentscrollHeight < scrollHeight) {
        //alert('calling...');
        for (var i = 0; i < 6; i++) {
            callData(count);//Once at bottom of page -> call 6 times
            count++;
        }
        currentscrollHeight = scrollHeight;
    }
});
function callData(counter) {
    $.ajax({
        type: "GET",
        url: "http://localhost:8000/get_event?id=" + counter,
        dataType: "html",
        success: function (result) {
            //alert(result[0]);
            $(result).appendTo('.list');
        },
        error: function (result) {}
    });
}
