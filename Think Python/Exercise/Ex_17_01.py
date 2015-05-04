# # Time object revisited

class Time(object):
    """represents the time of day.
       attributes: hour, minute, second"""
    # initialization
    def __init__(self, hour=0, minute=0, second=0):
        (self.hour, self.minute, self.second) = (hour, minute, second)
    # str method
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    # print
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
    # convert time to integer
    def time_to_int(self):
        minutes = self.hour*60 + self.minute
        seconds = minutes*60 + self.second
        return seconds
    # increment
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    # compare what time object is the later one
    def is_after(self, other):
        return (self.hour, self.minute, self.second) > (other.hour, other.minute, other.second)
    # + operator / type-based dispatch
    def __add__(self, other):
        if isinstance(other, Time):
            seconds = self.time_to_int() + other.time_to_int()
            return int_to_time(seconds)
        else:
            return self.increment(other)
    # right-side add
    def __radd__(self, other):
        return self.__add__(other)
    # Ex 18.1
    # __cmp__ method
    def __lt__(self, other):
        diff = self.time_to_int() - self.time_to_int()
        if diff < 0:
            return 1
        elif diff > 0:
            return -1
        else:
            return 0
    
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


        
# Test code
start = Time()

start.print_time()

print(start.time_to_int())

end = start.increment(1134)
end.print_time()

print(end.is_after(start))

start = Time(9,45)
duration = Time(1,35)
print(start+duration)

start = Time(9,45)
duration = Time(1,35)
print(start + duration)
print(start + 1337)
print(1337 + start)

print(start < start+duration)