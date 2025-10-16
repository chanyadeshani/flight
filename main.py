from flask import Flask, render_template, request, jsonify
import database
import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


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
    from_date = data.get('date_from')
    to_date = data.get('date_to')
    available_flights = [0, 0, 0, 0, 0, 0, 0]
    available_flights2 = ''
    if flightType.lower() == "one-way" or flightType.lower() == "round-trip":
        flight = [origin, destination, from_date]
        available_flights = database.get_flights('flight_old.db', flight[0], flight[1], flight[2])
        print("test", len(available_flights))

    return available_flights


@app.route('/confirm', methods=['POST'])
def customers():
    data = request.get_json()
    print("Request received:", request.json)
    first_name = data.get('first_name')
    second_name = data.get('second_name')
    last_name = data.get('last_name')
    phone_number = data.get('phone_number')
    email_address = data.get('email_address')
    address = data.get('address')
    passenger = [0, 0, 0, 0, 0, 0]

    passenger = database.add_pasenger('flight_old.db', first_name, second_name, last_name, phone_number, email_address,
                                      address)
    return passenger


@app.route('/customer', methods=('GET', 'POST'))
def customer():
    form = forms.CustomerForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Process form data if it's a POST request and form is valid
        # Save form data to the database
        first_name = form.first_name.data
        second_name = form.second_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        email_address = form.email_address.data
        address = form.address.data
        database.add_pasenger('flight_old.db', first_name, second_name, last_name, phone_number, email_address,
                              address)

        return render_template('flight_details_display.html')
    return render_template('Customer_details.html', form=form)


def get_booked_flight(flight_id):
    print('flight id = ', flight_id)
    flight = database.get_booked_flight('flight_old.db', flight_id)
    dept = ''
    if flight[0][1] == 'NRT':
        dept = 'Tokyo(NRT)'
    elif flight[0][1] == 'BMX':
        dept = 'Birmingham(BMX)'
    elif flight[0][1] == 'BRS':
        dept = 'Bristol(BRS)'
    elif flight[0][1] == 'EDI':
        dept = 'Edinburgh(EDI)'
    elif flight[0][1] == 'OXF':
        dept = 'Oxford(OXF)'
    else:
        dept = 'Zurich(ZRH)'

    dst = ''
    if flight[0][1] == 'NRT':
        dst = 'Tokyo(NRT)'
    elif flight[0][1] == 'BMX':
        dst = 'Birmingham(BMX)'
    elif flight[0][1] == 'BRS':
        dst = 'Bristol(BRS)'
    elif flight[0][1] == 'EDI':
        dst = 'Edinburgh(EDI)'
    elif flight[0][1] == 'OXF':
        dst = 'Oxford(OXF)'
    else:
        dept = 'Zurich(ZRH)'
    passenger = database.get_passenger('flight_old.db')

    print('flight from db', flight)
    print('passenger from db', passenger)
    return [
        {
            'first_name': passenger[0][1],
            'last_name': passenger[0][3],
            'departure': dept,
            'destination': dst,
            'time': flight[0][6],
            'price(GBP)': flight[0][3]
        }
    ]


@app.route('/get_booked_flight', methods=['POST'])
def get_booked_flight_route():
    data = request.get_json()
    flight_id = data.get('id')
    if flight_id:  # Check if flight_id is provided
        booked_flight = get_booked_flight(flight_id)
        return jsonify(booked_flight)
    else:
        return jsonify({'error': 'Flight ID not provided'}), 400


if __name__ == '__main__':
    database.init_database('flight_old.db')
    app.run(debug=True)
