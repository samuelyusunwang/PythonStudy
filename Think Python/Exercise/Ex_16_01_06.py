# Time object

class Time(object):
    """represents the time of day.
       attributes: hour, minute, second"""

# Ex 16.1
def print_time(time_obj):
    print('%.2d:%.2d:%.2d' % (time_obj.hour, time_obj.minute, time_obj.second))

# Ex 16.2
def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

# Ex 16.3
def increment(time, seconds):
    s = time.second + seconds
    time.second = s % 60
    m = time.minute + int(s/60)
    time.minute = m % 60
    time.hour += int(m/60)

# Ex 16.4
def increment_pure(time, seconds):
    t_new = Time()
    s = time.second + seconds
    t_new.second = s % 60
    m = time.minute + int(s/60)
    t_new.minute = m % 60
    t_new.hour = time.hour + int(m/60)
    return t_new

# Ex 16.5
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
def increment_planning(time, seconds):
    s = time_to_int(time)
    s = s + seconds
    return int_to_time(s)

# Ex 16.6
def mul_time(time, n):
    return int_to_time(time_to_int(time)*n)

def avg_pace(time, dist):
    return mul_time(time, 1/dist)


# Test code
t1 = Time(); t1.hour = 11; t1.minute = 59; t1.second = 30
print_time(t1)

t2 = Time(); t2.hour = 12; t2.minute = 0; t2.second = 0
print(is_after(t1, t2))

increment(t1, 60)
print_time(t1)

print_time(increment_pure(t1, 60))

print_time(increment_planning(t1, 60))

print_time(mul_time(t1, 2))

total_time = Time(); total_time.hour = 2; total_time.minute = 15; total_time.second = 25
print_time(avg_pace(total_time, 10))
