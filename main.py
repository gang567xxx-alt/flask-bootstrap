from flask import Flask,flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = b'gggggggggg'

car = [
    {'id':1, 'brand':'Toyota', 'model':'Yaris Ativ', 'year':2020, 'price':'570000'},
    {'id':2, 'brand':'Honda' , 'model':'Civic'     , 'year':2019, 'price':'890000'},
    {'id':3, 'brand':'Mazda' , 'model':'2'         , 'year':2021, 'price':'620000'}
]

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/cars', methods=['GET', 'POST'])#ค้นหารถตามยี่ห้อ 
def all_cars():

    if request.method == 'POST':
        brand = request.form['brand'].lower()
        tmp_car = []
        for cars in car:
            if cars['brand'].lower() == brand:
                tmp_car.append(cars)
        #car = tmp_car
        return render_template('cars/cars.html', title='Search Cars Page', cars=tmp_car)
    return render_template('cars/cars.html', title='Car List', cars=car)

@app.route('/cars/new', methods=['GET', 'POST'])
def new_car():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        year = request.form['year']
        price = request.form['price']

        if len(car) == 0:
            new_id = 1
        else:
            new_id = car[-1]['id'] + 1

        car.append({'id': new_id,'brand': brand,'model': model,'year': year,'price': price        })

        flash('เพิ่มรถใหม่เรียบร้อยแล้ว', 'success')
        return redirect(url_for('all_cars'))

    return render_template('cars/new_car.html', title='New Car')

@app.route('/cars/<int:id>/delete')
def delete_car(id):
    for c in car:
        if id == c['id']:
            car.remove(c)
            break

    flash('ลบรถเรียบร้อยแล้ว', 'success')
    return redirect(url_for('all_cars'))

@app.route('/cars/<int:id>/edit', methods=['GET', 'POST'])
def edit_car(id):
    selected_car = None

    for c in car:
        if c['id'] == id:
            selected_car = c
            break

    if selected_car is None:
        flash('ไม่พบรถที่ต้องการแก้ไข', 'error')
        return redirect(url_for('all_cars'))

    if request.method == 'POST':
        selected_car['brand'] = request.form['brand']
        selected_car['model'] = request.form['model']
        selected_car['year'] = request.form['year']
        selected_car['price'] = request.form['price']

        flash('แก้ไขข้อมูลเรียบร้อยแล้ว', 'success')
        return redirect(url_for('all_cars'))

    return render_template('cars/edit_car.html',title='Edit Car Page',car=selected_car)
