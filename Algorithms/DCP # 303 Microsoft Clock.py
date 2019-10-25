'''
This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
'''

def clock(time):
    hour, minute = time.split(':')
    angle = find_angle(int(hour), int(minute))
    return min(abs(angle), 360 - abs(angle)) 

def find_angle(hour, minute):
    degree_per_minute = 360 / 60
    degree_per_hour = 360 / 12
    # hour = hour + minute / 60 # optional, but if you need dynamic / accurate hour hand

    return (minute * degree_per_minute) - (hour * degree_per_hour)

print(clock('12:30')) # -> 180