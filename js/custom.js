$(document).ready(function(){
	var i = 0;
	var array = [];

	var test = $("ul img");
	console.log(test)


	$(".box2").hide(0);
	$(".box3").hide(0);
	$(".box4").hide(0);
	$(".box1").hide(0);
	// $(".box1").delay(10000).show();
	
	$.each(test, function(index, value){
		var timeDelay = 5000;
		setTimeout(function(){
		$(value).animate({marginLeft:-480},1000,function(){
			$(this).find("li:last").after($(this).find("li:first"));
			$(this).css({marginLeft:0});
		})

		}, timeDelay);
		// timeDelay = timeDelay * (index + 1)
		// console.log(timeDelay);
	})

})