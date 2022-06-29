import math


def get_time_components(input_time):
    return int(input_time.split(":")[0]), \
           int(input_time.split(":")[1].split(" ")[0]), \
           str(input_time.split(":")[1].split(" ")[1])


def addition(hh, offset, mm, offset_mm, am_pm):
    am_pm_mapper = {'AM': 'PM', 'PM': 'AM'}
    print(offset_mm)
    mm = mm + offset_mm
    if mm >= 60:
        mm = mm-60
        offset += 1
    for i in range(1, offset + 1):
        hh += 1
        if hh >= 12:
            am_pm = am_pm_mapper.get(am_pm)
            if hh > 12:
                hh = 1
    hh = str(hh).rjust(2, '0')
    mm = str(mm).rjust(2, '0')
    return hh+":"+mm+" "+am_pm


def time_calc(input_time: str, mins: int):
    if not input_time or not mins:
        return ""
    hh, mm, am_pm = get_time_components(input_time)
    split_time = math.modf(mins / 60)
    print(split_time)
    mm_new = round(split_time[0]*60)
    hh_new = round(split_time[1])
    print(mm_new)
    print(hh_new)
    return addition(hh, hh_new, mm, mm_new, am_pm)


ip = '09:13 AM'
mins = 200 # 3 : 20
res = time_calc(input_time=ip, mins=mins)
print(res)


""" 
97516204982

12:00 AM
01:00 AM
02:00 AM
03:00
11:00 PM
12:00PM
01:00 PM
AddMinutes(
Without using any built-in date or time functions, write a function or method that accepts two
mandatory arguments: the first argument is a 12-hour time string with the format "[H]H:MM
{AM|PM}", and the second argument is a (signed) integer. The second argument is the number of
minutes to add to the time of day represented by the first argument. The return value should be a
string of the same format as the first argument. For example, AddMinutes("9:13 AM", 200) would
return "12:33 PM". The exercise isn't meant to be too hard or take very long; we just want to see
how you code. Please use either Java or Scala to complete the assignment. Please include any test
cases that you write.
"""
#09: 13 AM, 200
#12: 33
"""
09:00 AM + 20

"""