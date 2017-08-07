import ephem
year =1923
while year <=1924:
    print (year)
    eq1 = ephem.next_spring_equinox(str(year))
    eq3 = ephem.next_autumn_equinox(str(year))
    eq2 = ephem.next_summer_solstice(str(year))
    eq4 = ephem.next_winter_solstice(str(year))
    eq5 = ephem.next_spring_equinox(str(year+1))
    print ("spring equinox: %s" % eq1)
    da = eq1
    while da<eq2:
        fm=ephem.next_full_moon(da)
        if fm > eq2:
            break
        print  ("  full moon: %s" % fm)
        da = fm
    print ("summer solstice: %s" % eq2)
    da = eq2
    while da<eq3:
        fm=ephem.next_full_moon(da)
        if fm > eq3:
            break
        print  ("  full moon: %s" % fm)
        da = fm
    print ("autumn equinox: %s" % eq3)
    while da<eq4:
        fm=ephem.next_full_moon(da)
        if fm > eq4:
            break
        print  ("  full moon: %s" % fm)
        da = fm
    print ("winter solstice: %s" % eq4)
    while da<eq5:
        fm=ephem.next_full_moon(da)
        if fm > eq5:
            break
        print  ("  full moon: %s" % fm)
        da = fm
    year += 1
