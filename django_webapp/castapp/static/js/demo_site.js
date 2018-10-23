function demo_file(){
		$.ajax({
			url : "/command",
			method: "get",
			success: function(res){
				$.notify({
					icon: 'glyphicon glyphicons-info-sign',
					title: 'The command sent was:', 
					message: res,
					target: '_blank'
				},{	
					type: "info",
					placement: {
						from: "bottom",
						align: "right"
					}
				});
			}
		});
}