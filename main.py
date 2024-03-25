from flask import Flask, render_template, request, jsonify
import database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_flights', methods=['POST'])
def submit_order():
    data = request.get_json()
    flightType = data.get('flightType')
    origin = data.get('origin')
    destination = data.get('destination')
    stops = data.get('stops')
    seats = data.get('seats')
    print("test")
    available_flights = [0,0,0,0,0]
    if flightType.lower() == "one-way":
        flight = [origin, destination]
        print(flight[0], flight[1])
        available_flights = database.get_flights('flight.db', flight[0],flight[1])
        print("test", len(available_flights))
        # Return a response (optional)
    return available_flights


if __name__ == '__main__':
    database.init_database('flight.db')
    app.run(debug=True)
