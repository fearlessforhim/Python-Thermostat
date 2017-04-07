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

    var centerY = 405;
    var centerX = 456;

    var timeout;
    
    $('.grabber').on('touchmove', function(e){
	$('.message .m').text("touch");
	var xPoint = event.touches[0].pageX;
	var yPoint = event.touches[0].pageY;
	$('.message .x').text(xPoint);
	$('.message .y').text(yPoint);
	$('.message .r').text(rotation);
	
	var divX = $('.wrapper').position().left;
	var divY = $('.wrapper').position().top;
//	var centerX = divX + 451;
//	var centerY = divY + 360;
	var rotation = Math.atan2(centerY - yPoint, centerX - xPoint) * 180 / Math.PI;
//	$('.cX').text(centerX);
//	$('.cY').text(centerY);
	if (rotation > -70 && rotation < 325) {   
	    $('.touch-box').css({'transform': 'rotate(' + (rotation-45) + 'deg)'});
	    var adjustedRotation = (rotation-45) + 90;
	    var degreeIncrease = adjustedRotation / 6;
	    var finalDegree = (55 + Math.ceil(degreeIncrease));
	    var celcius = ((finalDegree -32) * (5/9));
	    console.log("F Degree value: " + finalDegree);
	    console.log("C Degree value: " + celcius);
	    var hue = 30 + 240 * (30 - celcius) / 60;
	    $('.wrapper-back').css({'background-color': 'hsl(' + hue + ', 100%, 50%)'});
	    $('.wrapper-front .target .temperature').text(finalDegree);

	    if(timeout){
		clearTimeout(timeout);
	    }

	    timeout = setTimeout(function() {
		postTemperature(finalDegree);
	    }, 1000);
	}
	
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
	    contentType: 'application/json;charset=UTF-8',
	    success: function(data){
		currentStatusPoll(false)
	    }
	});
    }
    
    $('body').on('click', '.run-schedule', function(){
	$.ajax({
	    type: 'POST',
	    url: 'runSchedule',
	    success: function(data){
		currentStatusPoll(false)
	    }
	});
    });
    
    $('body').on('click', '.heat-control', function(){
	$.ajax({
	    type: 'POST',
	    url: 'toggleHeat',
	    success: function(data){
		currentStatusPoll(false)
	    }
	});
    });
    
    $('body').on('click', '.fan-control', function(){
	$.ajax({
	    type: 'POST',
	    url: 'toggleFan',
	    success: function(data){
		currentStatusPoll(false)
	    }
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
    
    function currentStatusPoll(repeat){
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
		//var targetTempElement = $('.temperature-display .temperature-display-wrapper .target .temperature');
		var wrapper = $('.temperature-display .temperature-display-wrapper');
		currentTempElement.html(temperature);
		//targetTempElement.html(target_temperature);
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

		if(repeat){
		    setTimeout(function(){currentStatusPoll(true)}, 5000);
		}
	    },
	    error: function(){
		window.location = '/thermostat'
	    }
	});
    };
    
    currentStatusPoll(true);
});
