def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value * (1 + rate_per_period)**periods

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

import math

def polygon_area(n, s):
    return (n*s**2)/(4*math.tan(math.pi/n))

print polygon_area(7,3)

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, 
    print point_y * scale

project_to_distance(2, 7, 4)