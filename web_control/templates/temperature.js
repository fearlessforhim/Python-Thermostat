$(function() {
	$('body').on('click', '.set-temperature', function(){
		console.log('clicked!');
		$.ajax({
			method: "POST",
			url: "setTemperature",
			data: 23
		});
	});
});
