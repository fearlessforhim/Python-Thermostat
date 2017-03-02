#/usr/bin/python

import datetime

def get_scheduled_target_temperature(data):
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    target_temperature = 70.0
    latest_valid_schedule_hour = -1
    latest_valid_schedule_minute = -1
    found_later_schedule = False
    day_of_week = str(datetime.datetime.today().weekday())
    schedules_for_day = data["schedules"][day_of_week]
    for sched in schedules_for_day:
        if sched["start"]["hour"] > current_hour:
            continue
        elif sched["start"]["hour"] == current_hour and sched["start"]["minute"] > current_minute:
            continue

        if sched["start"]["hour"] > latest_valid_schedule_hour:
            found_later_schedule = True
        elif sched["start"]["hour"] == latest_valid_schedule_hour and sched["start"][
            "minute"] >= latest_valid_schedule_minute:
            found_later_schedule = True

        if found_later_schedule:
            target_temperature = sched["temperature"]
            latest_valid_schedule_hour = sched["start"]["hour"]
            latest_valid_schedule_minute = sched["start"]["minute"]
            found_later_schedule = False
    return target_temperature