$(function(){
	var successAlert = '<div class="alert alert-success" role="alert"><strong>Sucess!</strong>The command has succesfully been sent to the server.</div>'
	var failedAlert = '<div class="alert alert-danger" role="alert"><strong>Ope!</strong>Something went wrong!  Please try again later!</div>'
	$(document).on('click', "#actionLink",function(){
			var link = $(this).attr('data');
			$.ajax({
				url: "execute/?command=" + link,
				type: 'GET',
				success: function(res) {
					var successAlert = '<div class="alert alert-success" role="alert"><strong>Sucess!</strong>The command has succesfully been sent to the server.</div>'
					$("#executeAlert").append(successAlert);
					
				}
		});
		});
	$(document).on('click  touchstart', "#actionPlay",function(){
			var data = "play"
			$.ajax({
				url: "/execute/?command=" + data,
				type: 'GET',
				success: function(res) {
					var successAlert = '<div class="alert alert-success" role="alert"><strong>Sucess!</strong>The command has succesfully been sent to the server.</div>'
					$("#executeAlert").append(successAlert);
				}
		});
		});
	$(document).on('click  touchstart', "#actionPause",function(){
			var data = "pause"
			$.ajax({
				url: "/execute/?command=" + data,
				type: 'GET',
				success: function(res) {
					var successAlert = '<div class="alert alert-success" role="alert"><strong>Sucess!</strong>The command has succesfully been sent to the server.</div>'
					$("#executeAlert").append(successAlert);
				}
		});
		});
});
