$(function(){
	handled = false;
	function sendRequest(data){
		$.ajax({
			url: "execute/?command=" + data,
			type: 'GET',
			success: function(res) {
				
				console.log(res)
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
				demo_file();
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
	};
	
	$(document).on('click touchstart', "#actionLink",function(e){
			var link = $(this).attr('data');
			
			if(e.type == 'touchstart'){
				sendRequest(link);
				handled = true;
			}
			else if(handled == false){
				sendRequest(link);
			}
			
	});
	
	$(document).on('click  touchstart', "#actionPlay",function(e){
			var data = "play"
			if(e.type == 'touchstart'){
				sendRequest(data);
				handled = true;
			}
			else if(handled == false){
				sendRequest(data);
			}
	});
	
	$(document).on('click  touchstart', "#actionPause",function(e){
			var data = "pause"
			if(e.type == 'touchstart'){
				sendRequest(data);
				handled = true;
			}
			else if(handled == false){
				sendRequest(data);
			}
	});
});
