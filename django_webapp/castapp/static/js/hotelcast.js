$(function(){
	$(document).on('click', "#actionLink",function(){
			var link = $(this).attr('data');
			$.ajax({
				url: "execute/?command=" + link,
				type: 'GET',
				success: function(res) {
					alert(res.success_message);
					console.log(res.success_message);
				}
		});
		});
	$(document).on('click  touchstart', "#actionPlay",function(){
			var data = "play"
			$.ajax({
				url: "/hotelcast/execute/?command=" + data,
				type: 'GET',
				success: function(res) {
					alert(res.success_message);
					console.log(res.success_message);
				}
		});
		});
	$(document).on('click  touchstart', "#actionPause",function(){
			var data = "pause"
			$.ajax({
				url: "/hotelcast/execute/?command=" + data,
				type: 'GET',
				success: function(res) {
					alert(res.success_message);
					console.log(res.success_message);
				}
		});
		});
});
