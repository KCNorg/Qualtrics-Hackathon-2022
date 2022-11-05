reviews = {
    "wifiService": "Wifi Service",
    "timeConvenient": "Time Convenient",
    "bookingEase": "Booking Ease",
    "gateLocation": "Gate Location",
    "food": "Food",
    "boarding": "Boarding",
    "seatComfort": "Seat Comfort",
    "entertainment": "Entertainment",
    "onboardService": "Onboard Service",
    "legRoomService": "Leg Room Service",
    "baggageHandling": "Baggage Handling",
    "checkinService": "CheckinService",
    "inflightService": "Inflight Service",
    "cleanliness": "Cleanliness",
    "departureDelayInMinutes": "Departure Delay In Minutes",
    "arrivalDelayInMinutes": "Arrival Delay In Minutes",
}


inv_reviews = {v: k for k, v in reviews.items()}

reviews_reverse = {
    "Wifi Service": "wifiService",
    "Time Convenient": "timeConvenient",
    "Booking Ease": "bookingEase",
    "Gate Location": "gateLocation",
    "Food": "food",
    "Boarding": "boarding",
    "Seat Comfort": "seatComfort",
    "Entertainment": "entertainment",
    "Onboard Service": "onboardService",
    "Leg Room Service": "legRoomService",
    "Baggage Handling": "baggageHandling",
    "CheckinService": "checkinService",
    "Inflight": "inflightService",
    "Cleanliness": "cleanliness",
    "Departure Delay In Minutes": "departureDelayInMinutes",
    "Arrival Delay In Minutes": "arrivalDelayInMinutes",
}

info = {
    "travelType": {
        "name": "Travel Type",
        "values": ["Personal Travel", "Business Travel"]
    },
    "travelClass": {
        "name": "Travel Class",
        "values": ["Business", "Eco", "Eco Plus"]
    },
    "travelDistance": {
        "name": "Travel Distance",
        "values": ["Short", "Middle", "Long"]
    },
    "gender": {
        "name": "Gender",
        "values": ["Female", "Male"]
    },
    "type": {
        "name": "Passenger Type",
        "values": ["Loyal Customer", "Disloyal Customer"]
    },
    "age": {
        "name": "Age",
        "values": ["Child", "Young Adult", "Mid Adult", "Elder"]
    }
}

reverse_parser = {
    "Personal Travel": "travelType",
    "Business Travel": "travelType",
    "Business": "travelClass",
    "Eco": "travelClass",
    "Eco Plus": "travelClass",
    "Short": "travelDistance",
    "Middle": "travelDistance",
    "Long": "travelDistance",
    "Female": "gender",
    "Male": "gender",
    "Loyal customer": "type",
    "Disloyal Customer": "type",
    "Child": "Age",
    "Young Adult": "Age",
    "Mid Adult": "Age",
    "Elder": "Age"
}


def revert_name(d, name):
    new_d = d.copy()
    new_d['name'] = name
    return new_d


inv_info = {v['name']: revert_name(v, k) for k, v in info.items()}


def age_to_group(age):
    if age < 18:
        return "Child"
    elif age < 35:
        return "Young adult"
    elif age < 50:
        return "Mid adult"
    else:
        return "Elder"



def flight_distance_to_group(flight_distance):
    if flight_distance < 500:
        return "Short"
    elif flight_distance < 1750:
        return "Middle"
    else:
        return "Long"
