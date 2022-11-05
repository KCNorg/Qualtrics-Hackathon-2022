from flask import Flask, jsonify

app = Flask(__name__)

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


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/types', methods=['GET'])
def get_types():
    jdata = dict()
    jdata['review'] = list(reviews.values())
    jdata['info'] = [dict(name=col_info['name'], values=col_info['values']) for col_info in info.values()]
    return jsonify(jdata)

if __name__ == '__main__':
    app.run()
