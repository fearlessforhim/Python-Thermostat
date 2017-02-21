$(function() {
    $('body').on('click', '.temp-up', function(){
        var temperature = $('[name="Temperature"]').val()
        temperature++;
        $('[name="Temperature"]').val(temperature);
        postTemperature(temperature)
    });
    
    $('body').on('click', '.temp-dow', function(){
        var temperature = $('[name="Temperature"]').val()
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

	function currentStatusPoll(){
		$.ajax({
			type: 'GET',
			url: 'currentState',
			success: function(data){
				var temperature = data['curTemp'];
				var temporary = data['usingTemporary']
                var target_temperature = data['targetTemp']
				$(".display-current .temperature").html(temperature);
				$(".display-target .temperature").html(target_temperature);
				if(temporary){
					$(".temperature-display .display-target").addClass("temporary");
				} else{
					$(".temperature-display .display-target").removeClass("temporary");
                }
				setTimeout(currentStatusPoll, 500);
			}
		});
	};

	currentStatusPoll();
});
