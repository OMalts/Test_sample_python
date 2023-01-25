from math import pi
def circle_area(radius):
    if type (radius) not in [int, float ,bool]:
        raise ValueError("wrong radius variable format")
    if radius <0:
        raise ValueError ("radius can't be negative")
    return pi*radius**2

# radius_list = [25,0, -5, +2j, False, [3,3], 'one' ]
# message = 'Circle surfase {radius} --> {area}'

# for r in radius_list:
#     s=circle_area(r)
#     print(message.format(radius = r, area = s))
