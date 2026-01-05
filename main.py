from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

car = [
    {'id':1, 'brand':'Toyota', 'model':'Yaris Ativ', 'year':2020, 'price':'570000'},
    {'id':2, 'brand':'Honda' , 'model':'Civic'     , 'year':2019, 'price':'890000'},
    {'id':3, 'brand':'Mazda' , 'model':'2'         , 'year':2021, 'price':'620000'}
]

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/cars')
def all_cars():
    return render_template('cars/cars.html', title='Car List', cars=car)

@app.route('/cars/new', methods=['GET', 'POST'])
def new_car():
    if request.method == 'POST':
        brend = request.form['brand']
        model = request.form['model']
        year = request.form['year']
        price = request.form['price']

        length = len(car)
        id = car[length - 1]['id'] + 1

        car.append({'id': id, 'brand': brend, 'model': model, 'year': year, 'price': price})

        car.append(car)

        return redirect(url_for('all_cars'))
    return render_template('cars/new_car.html', title='New Car')