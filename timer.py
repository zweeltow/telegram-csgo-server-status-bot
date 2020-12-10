import datetime
import time

class Timer:
    wanted_day = 'wednesday'
    wanted_time = 00

    list = [['monday', 0],['tuesday', 1],['wednesday', 2],['thursday', 3],['friday', 4],['saturday', 5],['sunday', 6]]

    for i in list:
        if wanted_day == i[0]:
            number_wanted_day = i[1]

    today = datetime.datetime.today().weekday() # today delivers the actual day

    delta_days = number_wanted_day - today # delta_days describes how many days are left until the wanted day

    time = time.localtime(time.time()) # time delivers the actual time

    if wanted_time > time[3]:
        delta_hours = wanted_time - time[3]
        delta_mins = 59 - time[4]
        delta_secs = 59 - time[5]

    else:
        delta_days = delta_days - 1
        delta_hours = 23 - time[3] + wanted_time
        delta_mins = 59 - time[4]
        delta_secs = 59 - time[5]
        
    if delta_days < 0:
        delta_days = delta_days + 7
    
    return delta_days, delta_hours, delta_mins, delta_secs
