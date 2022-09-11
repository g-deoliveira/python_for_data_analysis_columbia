x = 10

if x is None:
    print('x is None')
elif not isinstance(x, int):
    print('x is not an integer')
elif x < 0:
    print('x is negative')
elif x > 0:
    print('x is positive')
else:
    print('x is zero')

y = -8

if y is None:
    print('y is None')
elif not isinstance(y, int):
    print('y is not an integer')
else:
    # y is an integer
    if y < 0:
        print('y is negative')
        if y % 2 == 0:
            print('y is even')
        else:
            print('y is odd')
    elif y > 0:
        print('y is positive')
        if y % 2 == 0:
            print('y is even')
        else:
            print('y is odd')
    else:
        print('y is zero')

temperature = 33
precipitation_probability = 45
snow_probability = 45
wind_speed = 45
wind_gust = 62

if temperature < 40 and precipitation_probability > 66 and snow_probability > 66 and wind_speed > 45 and wind_gust > 60:
    cancel_race = True
else:
    cancel_race = False

if (temperature < 40 and precipitation_probability > 66
        and snow_probability > 66 and wind_speed > 45 and wind_gust > 60):
    cancel_race = True
else:
    cancel_race = False
