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
        "name": "Name",
        "values": ["Female", "Male"]
    },
    "type": {
        "name": "Passenger Type",
        "values": ["Loyal customer, Disloyal Customer"]
    },
    "age": {
        "name": "Age",
        "values": ["Child", "Young Adult", "Mid Adult", "Elder"]
    }
}


def age_to_group(age):
    if age < 18:
        return "child"
    elif age < 35:
        return "young adult"
    elif age < 50:
        return "mid adult"
    else:
        return "elder"

def flight_distance_to_group(flight_distance):
    if flight_distance < 500:
        return "short"
    elif flight_distance < 1750:
        return "middle"
    else:
        return "long"
