$(function(){
	$(document).on('click touchstart', "#actionLink",function(){
			var link = $(this).attr('data');
			$.ajax({
				url: "execute/?command=" + link,
				type: 'GET',
				success: function(res) {
					$.notify({
						icon: 'glyphicon glyphicons-check',
						title: 'Sucess!',
						message: 'The command has ben sent to the sever!',
						target: '_blank'
					},{	
						type: "success",
						placement: {
							align: "center"
						}
					});
					
				},
				error: function(res) {
					$.notify({
						icon: 'glyphicon glyphicons-warning-sign',
						title: 'Ope!',
						message: 'There was an error of some sort please try again!',
						target: '_blank'
					},{	
						type: "danger",
						placement: {
							align: "center"
						}
					});
				}
		});
		});
	$(document).on('click  touchstart', "#actionPlay",function(){
			var data = "play"
			$.ajax({
				url: "/execute/?command=" + data,
				type: 'GET',
				success: function(res) {
					$.notify({
						// options
						icon: 'glyphicon glyphicons-check',
						title: 'Sucess!',
						message: 'The command has ben sent to the sever!',
						target: '_blank'
					},{	
						type: "success",
						placement: {
							align: "center"
						}
					});
				}
		});
		});
	$(document).on('click  touchstart', "#actionPause",function(){
			var data = "pause"
			$.ajax({
				url: "/execute/?command=" + data,
				type: 'GET',
				success: function(res) {
					$.notify({
						// options
						icon: 'glyphicon glyphicons-check',
						title: 'Sucess!',
						message: 'The command has ben sent to the sever!',
						target: '_blank'
					},{	
						type: "success",
						placement: {
							align: "center"
						}
					});
				}
				
		});
		});
});
