from flask import Flask, flash, redirect, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'clave_secreta_mwdcdw2c312'

# conexion to db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'web_flask'

mysql = MySQL(app)


# context processor
@app.context_processor
def  date_now():
    return {
        'now': datetime.utcnow()
    }

# endPoints


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/information')
@app.route('/information/<string:name>')
def information(name = None):

    text = "<strong>information, do not have a name</strong>"
    if name:
        text = f"<h1>information {name}</h1>"

    return render_template('information.html', 
                            text=text
                            )




@app.route('/contact')
@app.route('/contact/<redirection>')
def contact(redirection = None):
   
    text = "<h1>contact</h1>"
    if redirection:
        return render_template('contact.html', 
                            text=text
                            )
    else:
        return redirect(url_for('information'))


@app.route('/create-car', methods=['GET', 'POST'])
def create_car():

    if request.method == 'POST':

        brand    = request.form['brand']
        model    = request.form['model']
        price    = request.form['price']
        location = request.form['location']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO cars VALUES(NULL, %s, %s, %s, %s)", (brand, model, price, location))
        cursor.connection.commit()
        
        flash('A New Car has been created')
        return redirect(url_for('index'))

    return render_template('create_car.html', text='lola')

@app.route('/cars')
def cars():
    cursor = mysql.connection.cursor()
    cursor.execute("select * FROM cars")
    cars = cursor.fetchall()
    cursor.close()

    return render_template('cars.html', cars = cars)

@app.route('/car/<car_id>')
def car(car_id):
    cursor = mysql.connection.cursor()
    cursor.execute("select * FROM cars WHERE id = %s", (car_id))
    car = cursor.fetchall()
    cursor.close()

    return render_template('car.html', car = car[0])

if __name__ == '__main__':
    app.run(debug=True)

