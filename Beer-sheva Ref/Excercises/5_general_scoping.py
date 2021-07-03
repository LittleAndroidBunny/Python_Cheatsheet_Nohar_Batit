def stupid_function(x):
    y = 2*x
    return y


z = 1
v = stupid_function(z)
print(v)
# print(y)  # Will this work?
# print(x)  # Will this work?

KILOMETERS_TO_METERS = 1000
METERS_TO_KILOMETERS = 1000

HOURS_TO_SECONDS = 3600


def convert_velocity_to_si(velocity):
    """takes velocity in km/h and returns velocity in m/s"""
    return velocity*KILOMETERS_TO_METERS/HOURS_TO_SECONDS


v = 100  # km/h
print(convert_velocity_to_si(v))


