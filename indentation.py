# according to Pep-8:
#   use 4 spaces for indentation

vehicle = 'Honda CRV'
door_count = 4

sunroof = True # does the vehicle have a sunroof
roof_rack = True # does the vehicle have a roof rack
roof_rack_for_skis = False
roof_rack_for_bike = True

print('You are driving a ', vehicle)

if door_count == 4:
    print('Your vehicle has', door_count, 'doors.')
else:
    print('Your vehicle does not have 4 doors.')
if sunroof:
    print('Your vehicle has a sunroof.')
else:
    print('Your vehicle does not have a sunroof.')

if roof_rack:
    print('Your vehicle has a roof rack.')
    if roof_rack_for_skis:
        print('The roof rack can transport skis.')
    elif roof_rack_for_bike:
        print('The roof rack can transport bikes.')
    else:
        print('The roof rack is a standard roof rack.')
else:
    print('The vehicle does not have a roof rack.')
