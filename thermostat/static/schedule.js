$(function() {
    $.ajax({
	url: 'schedule_data',
	type: 'GET',
	success: function(data){    
	    render(data);
	}
    });
    
    function render(data){
	console.log(data);
	var daily_schedules = data['schedules'];
	var sorted_schedules = {};
	var dayNames = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	for(var x = 0; x < 7; x++){
	    var dayName = dayNames[x];
	    var day = daily_schedules[''+x];
	    var dayRowClone = $("#schedule-day-template .day-row").clone();
	    dayRowClone.find('.day').text(dayName);
	    $(".schedule-control").append(dayRowClone);
	    for(item in day){
		console.log(day[item].start.hour);
		var startHour = day[item].start.hour;
		var startMin = day[item].start.minute;
		var temperature = day[item].temperature;
		var schedRowClone = $('#schedule-row-template .row-id').clone();
		schedRowClone.attr('data-dayid',x);
		schedRowClone.find('.start-hour').text(startHour == "0" ? "00": startHour);
		schedRowClone.find('.start-minute').text(startMin == "0" ? "00": startMin);
		schedRowClone.find('.temperature').text(temperature);
		$('.schedule-control').append(schedRowClone);
	    }
	}
    }
    
    function sort(a,b) {
	if (asc) {
	    return (a[prop] > b[prop]) ? 1 : ((a[prop] < b[prop]) ? -1 :0 );
	} else {
	    return (a[prop] < b[prop]) ? 1 : ((a[prop] > b[prop]) ? -1 :0 );
	}
    }
    
    $('body').on('click', '.sched-temp-up', function(){
	var me = $(this);
	var temp = parseInt(me.parents('.row-id').find('.temperature').html());
	updateTemperature(me, temp + 1);
    });
    
    $('body').on('click', '.sched-temp-down', function(){
	var me = $(this);
	var temp = parseInt(me.parents('.row-id').find('.temperature').html());
	updateTemperature(me, temp - 1);
    });
    
    function updateTemperature(btn, newTemp) {
	btn.parents('.row-id').find('.temperature').html(newTemp);
    }
    
    
    $('body').on('click', '.time-up', function(){
	var me = $(this);
	var hour = parseInt(me.parents('.row-id').find('.start-hour').html());
	var minute = parseInt(me.parents('.row-id').find('.start-minute').html());
	if(minute == 45 && hour == 23)
	    return;
	if(minute == 45) {
	    minute = 0;
	    hour = hour + 1;
	} else {
	    minute = minute + 15;
	}
	
	updateTime(me, hour, minute);
    });
    
    $('body').on('click', '.time-down', function(){
	var me = $(this);
	var hour = parseInt(me.parents('.row-id').find('.start-hour').html());
	var minute = parseInt(me.parents('.row-id').find('.start-minute').html());
	if(minute == 0 && hour == 0)
	    return;
	if(minute == 0) {
	    minute = 45;
	    hour = hour - 1;
	} else {
	    minute = minute - 15;
	}
	
	updateTime(me, hour, minute);
    });
    
    function updateTime(btn, newHour, newMinute) {
	btn.parents('.row-id').find('.start-hour').html(newHour == 0 ? "00" : newHour);
	btn.parents('.row-id').find('.start-minute').html(newMinute == 0 ? "00" : newMinute);
    }
});
