$(function() {
	$('body').on('click', '.temp-up', function(){
		var temperature = parseInt($('.display-target .temperature .value').html())
		temperature++;
		$('[name="Temperature"]').val(temperature);
		postTemperature(temperature)
		});
		
		$('body').on('click', '.temp-down', function(){
		var temperature = parseInt($('.display-target .temperature .value').html())
		temperature;
		$('[name="Temperature"]').val(temperature);
		postTemperature(temperature)
	});
		
	function postTemperature(temperature) {
		$.ajax({
		    type: 'POST',
		    url: 'setTemperature',
		    data: JSON.stringify(
		        {
		            'temperature': temperature
		        }
		    ),
		    contentType: 'application/json;charset=UTF-8'
		});
	}

	$('body').on('click', '.run-schedule-button', function(){
		$.ajax({
			type: 'POST',
			url: 'runSchedule'
		});
	});

	$('body').on('click', '.heat-toggle', function(){
		$.ajax({
			type: 'POST',
			url: 'toggleHeat'
		});
	});
	
	$('body').on('click', '.fan-toggle', function(){
		$.ajax({
			type: 'POST',
			url: 'toggleFan'
		});
	});

	$('body').on('click', '.modify-schedule-btn', function(){
		window.location = '/schedule';
	});

	function currentStatusPoll(){
		$.ajax({
			type: 'GET',
			url: 'currentState',
			success: function(data){
				var temperature = data['curTemp'];
				var temporary = data['usingTemporary'];
                		var target_temperature = data['targetTemp'];
				var is_heat_on = data['isHeatOn'];
				var is_allowing_heat = data['allowingHeat'];
				var is_allowing_fan = data['allowingFan'];

				$(".display-current .temperature .value").html(temperature);
				$(".display-target .temperature .value").html(target_temperature);
				if(temporary){
					$(".temperature-display .display-target").addClass("temporary");
				} else {
					$(".temperature-display .display-target").removeClass("temporary");
                		}

				var currentDisplay = $(".display-current");
				if(is_heat_on) {
					currentDisplay.addClass("heat-on");
				} else {
					currentDisplay.removeClass("heat-on");
				}

				var heatToggle = $(".heat-toggle");
				if(is_allowing_heat) {
					heatToggle.addClass("heat-on");
					heatToggle.removeClass("heat-off");
				} else {
					heatToggle.addClass("heat-off");
					heatToggle.removeClass("heat-on");

				}

				var fanToggle = $(".fan-toggle");
				if(is_allowing_fan) {
					fanToggle.addClass("fan-on");
					fanToggle.removeClass("fan-off");
				} else {
					fanToggle.addClass("fan-off");
					fanToggle.removeClass("fan-on");

				}

				setTimeout(currentStatusPoll, 500);
			}
		});
	};

	currentStatusPoll();
});
