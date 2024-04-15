from flask import Flask, render_template, request, jsonify
import database
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length

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
        available_flights = database.get_flights('flight.db', flight[0], flight[1], flight[2])
        print("test", len(available_flights))

    return available_flights


@app.route('/confirm')
def customers():
    return "<H1> Successful</H1>"


@app.route('/customer', methods=('GET', 'POST'))
def customer():
    form = forms.CustomerForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Process form data if it's a POST request and form is valid
        # Example: Save form data to the database
        return 'Form submitted successfully!'
    return render_template('Customer_details.html', form=form)


if __name__ == '__main__':
    database.init_database('flight.db')
    app.run(debug=True)
