import ephem
import datetime
syear = 2017
eyear = 2030
year = syear
while year <= eyear:
    fm1=ephem.next_full_moon(str(year)+"/1/1")
    print (str(year))
    nyear = year
    while year == nyear:
        fm2=ephem.next_full_moon(fm1)
        nyear=fm2.datetime().year
        if fm1.datetime().month == fm2.datetime().month:
            print("  "+str(fm1.datetime().month))
            print ("    1st:",fm1)
            print ("    2nd:",fm2)
        fm1=fm2
    print ("-----")
    year += 1
