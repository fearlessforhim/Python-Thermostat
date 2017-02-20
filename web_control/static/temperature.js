$(function() {
	$('body').on('click', '.set-temperature', function(){
		var temperature = $('[name="Temperature"]').val()
		$.ajax({
			type: 'POST',
			url: 'setTemperature',
			data: JSON.stringify({'temperature':temperature}),
			contentType: 'application/json;charset=UTF-8'
		});
	});

	$('body').on('click', '.run-schedule-button', function(){
		$.ajax({
			type: 'POST',
			url: 'runSchedule'
		});
	});
});
