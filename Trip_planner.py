def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475
    else:
        print "Invalid input madafaka"
def rental_car_cost(days):
    car_cost = 40*days
    if days>=7:
        car_cost -= 50
    elif days>=3:
        car_cost -= 20
    return car_cost
def trip_cost(city,days,spending_money):
    return hotel_cost(days)+rental_car_cost(days)+plane_ride_cost(city)+spending_money

print trip_cost("Los Angeles",5,600)
