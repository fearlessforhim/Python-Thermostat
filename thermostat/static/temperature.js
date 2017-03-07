$(function() {
    $('body').on('click', '.temp-up', function(){
	var tempElement = $('.temperature-display .temperature-display-wrapper .target .temperature');
	var temperature = parseInt(tempElement.html());
	temperature++;
	postTemperature(temperature);
    });
    
    $('body').on('click', '.temp-down', function(){
	var tempElement = $('.temperature-display .temperature-display-wrapper .target .temperature');
	var temperature = parseInt(tempElement.html());
	temperature--;
	postTemperature(temperature);
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
    
    $('body').on('click', '.run-schedule', function(){
	$.ajax({
	    type: 'POST',
	    url: 'runSchedule'
	});
    });
    
    $('body').on('click', '.heat-control', function(){
	$.ajax({
	    type: 'POST',
	    url: 'toggleHeat'
	});
    });
    
    $('body').on('click', '.fan-control', function(){
	$.ajax({
	    type: 'POST',
	    url: 'toggleFan'
	});
    });
    
    $('body').on('click', '.schedule-page-btn', function(){
	$('.temperature-control').addClass('hidden');
	$('.schedule-control').removeClass('hidden');
    });

    $('body').on('click', '.thermostat-page-btn', function(){
	$('.temperature-control').removeClass('hidden');
	$('.schedule-control').addClass('hidden');
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
		
		var currentTempElement = $('.temperature-display .temperature-display-wrapper .current .temperature');
		var targetTempElement = $('.temperature-display .temperature-display-wrapper .target .temperature');
		var wrapper = $('.temperature-display .temperature-display-wrapper');
		currentTempElement.html(temperature);
		targetTempElement.html(target_temperature);
		if(temporary){
		    wrapper.addClass("temporary");
		} else {
		    wrapper.removeClass("temporary");
                }
		
		if(is_heat_on) {
		    wrapper.addClass("running");
		} else {
		    wrapper.removeClass("running");
		}
		
		var heatToggle = $(".heat-control .control");
		if(is_allowing_heat) {
		    heatToggle.addClass("on");
		    heatToggle.removeClass("off");
		} else {
		    heatToggle.addClass("off");
		    heatToggle.removeClass("on");
		    
		}
		
		var fanToggle = $(".fan-control .control");
		if(is_allowing_fan) {
		    fanToggle.addClass("on");
		    fanToggle.removeClass("off");
		} else {
		    fanToggle.addClass("off");
		    fanToggle.removeClass("on");
		    
		}
		
		setTimeout(currentStatusPoll, 500);
	    }
	});
    };
    
    currentStatusPoll();
});
