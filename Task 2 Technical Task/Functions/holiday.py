def hotelCost(nights):
    return nights * 200

def planeCost(place):
    if "France" == place:
        return 500
    elif "Canada" == place:
        return 300
    elif "States" == place:
        return 400
    else:
        return 50
    

def carRental(days):
    return days * 50
  
    


place = input("Where are you going: ")
nights = int(input("How many nights are you staying: "))
days = int(input("How many days do you need to rent the: "))   

def holidayCost(nights, place, days):
    return hotelCost(nights) + planeCost(place) + carRental(days)
print(holidayCost(nights, place, days))