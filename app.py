from flask import Flask, render_template, session, request, redirect, url_for
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors

mysql = MySQL()
app = Flask(__name__, template_folder='templates')
app.secret_key = 'secretkey'

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'dbdesignfinal'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/', methods=['GET'])
def home():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM mslocation")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', locations=data)

@app.route('/profile/book')
def profile():
    if 'loggedin' in session:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM msreservation mr JOIN msguest mg ON mg.GuestID = mr.GuestID JOIN msroom rm ON rm.RoomID = mr.RoomID JOIN mslocation ml ON ml.LocationID = mr.LocationID WHERE mr.GuestID = %s AND mr.PaymentStatus = 'Complete'", session['id'])
        data = cur.fetchall()
        cur.close()
        
    return render_template('profile.html', bookings=data)

@app.route('/profile/payment')
def profilePay():
    if 'loggedin' in session:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM msreservation mr JOIN msguest mg ON mg.GuestID = mr.GuestID JOIN msroom rm ON rm.RoomID = mr.RoomID JOIN mslocation ml ON ml.LocationID = mr.LocationID WHERE mr.GuestID = %s AND mr.PaymentStatus = 'Pending'", session['id'])
        data = cur.fetchall()
        cur.close()
    
    return render_template('profilePay.html', bookings=data)

@app.route('/profile/payment/pay/<int:id>')
def profilePayed(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("UPDATE msreservation SET PaymentStatus = 'Complete' WHERE ReservationID = %s", id)
    conn.commit()
    cur.close()

    return redirect(url_for('profilePay'))

@app.route('/profile/delete/<int:id>')
def profileDelete(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("DELETE FROM msreservation WHERE ReservationID = %s", id)
    conn.commit()
    text = 'data deleted successfully'

    return redirect(url_for('profile'))

@app.route('/profile/update/<int:id>', methods=['GET', 'POST'])
def updateBook(id):
    text = ''
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM msreservation mr JOIN msguest mg ON mg.GuestID = mr.GuestID JOIN msroom rm ON rm.RoomID = mr.RoomID JOIN mslocation ml ON ml.LocationID = mr.LocationID WHERE mr.reservationID = %s", id)
    data = cur.fetchone()

    if request.method == 'POST':
        roomtype = request.form['RoomType']
        paymenttype = request.form['PaymentType']
        checkindate = request.form['CheckIn']
        checkoutdate = request.form['CheckOut']

        cur.execute("UPDATE msreservation SET RoomType = %s, PaymentType = %s, CheckIn = %s, CheckOut = %s WHERE ReservationID = %s", (roomtype, paymenttype, checkindate, checkoutdate, id,))
        conn.commit()

        text = 'Data updated successfully'

    return render_template('profileUpdate.html', data=data, text=text)

@app.route('/adminPage', methods=['GET'])
def adminHome():
    if 'loggedinn' in session:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM msreservation mr JOIN msguest mg ON mg.GuestID = mr.GuestID JOIN msroom rm ON rm.RoomID = mr.RoomID JOIN mslocation ml ON ml.LocationID = mr.LocationID ORDER BY mr.GuestID")
        data = cur.fetchall()
        cur.close

        return render_template('adminPage.html', reservations=data)

    return render_template('adminPage.html')

@app.route('/adminPage/guest')
def adminGuest():
    if 'loggedinn' in session:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM msguest")
        data = cur.fetchall()
        cur.close

    return render_template('adminGuest.html', guests=data)

@app.route('/adminPage/location')
def adminLocation():
    if 'loggedinn' in session:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM mslocation")
        data = cur.fetchall()
        cur.close

    return render_template('adminLocation.html', locations=data)

@app.route('/adminPage/location/add', methods=['GET', 'POST'])
def adminAdd():
    if request.method == 'POST' and 'Location' in request.form and 'LocationName' in request.form and 'LocationAddress' in request.form and 'LocationDescription' in request.form:
        region = request.form['Location']
        hotel = request.form['LocationName']
        address = request.form['LocationAddress']
        description = request.form['LocationDescription']

        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("INSERT INTO mslocation VALUES(NULL, %s, %s, %s, %s)", (hotel, address, description, region,))
        conn.commit()
        cur.close()

        return redirect(url_for('adminLocation'))
    elif request.method == 'POST':
        text = "Please fill in all the forms"
    
    return render_template('/adminAdd.html')

@app.route('/adminPage/location/update/<int:id>', methods=['GET', 'POST'])
def adminUpdate(id):
    text = ''
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM mslocation WHERE LocationID = %s", id)
    data = cur.fetchone()

    if request.method == 'POST' and 'Location' in request.form and 'LocationName' in request.form and 'LocationAddress' in request.form and 'LocationDescription' in request.form:
        region = request.form['Location']
        hotel = request.form['LocationName']
        address = request.form['LocationAddress']
        description = request.form['LocationDescription']

        cur.execute("UPDATE mslocation SET LocationName = %s, LocationAddress = %s, LocationDescription = %s, Location = %s WHERE LocationID = %s", (hotel, address, description, region, id,))
        conn.commit()

        return redirect(url_for('adminLocation'))

    return render_template('adminUpdate.html', cur=data)

@app.route('/adminPage/location/delete/<int:id>')
def adminDelete(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("DELETE FROM mslocation WHERE LocationID = %s", id)
    conn.commit()
    text = 'data deleted successfully'

    return redirect(url_for('adminLocation'))

@app.route('/add', methods=['GET', 'POST'])
def addBooking():
    text = ''
    if request.method == 'POST' and 'RoomType' in request.form and 'PaymentType' in request.form and 'CheckIn' in request.form and 'CheckOut' in request.form:
        roomtype = request.form['RoomType']
        paymenttype = request.form['PaymentType']
        checkindate = request.form['CheckIn']
        checkoutdate = request.form['CheckOut']

        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("INSERT INTO msreservation VALUES(NULL, %s, %s, 'Waiting for Payment', %s, %s, %s, 'ST001')", (roomtype, paymenttype, checkindate, checkoutdate, session['id'],))
        conn.commit()
        cur.close()
        text = "Account successfully created!"
    elif request.method == 'POST':
        text = "Please fill in all the forms"
    
    return render_template('addBooking.html', text=text)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def updateBooking(id):
    text = ''
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM msreservation WHERE ReservationID = %s", id)
    data = cur.fetchone()

    if request.method == 'POST':
        roomtype = request.form['RoomType']
        paymenttype = request.form['PaymentType']
        checkindate = request.form['CheckIn']
        checkoutdate = request.form['CheckOut']

        cur.execute("UPDATE msreservation SET RoomType = %s, PaymentType = %s, CheckIn = %s, CheckOut = %s WHERE ReservationID = %s", (roomtype, paymenttype, checkindate, checkoutdate, id,))
        conn.commit()

        text = 'Data updated successfully'

    return render_template('updateBooking.html', data=data, text=text)

@app.route('/login', methods=['GET', 'POST'])
def userLogin():
    text = ''
    if request.method == 'POST' and 'GuestUsername' in request.form and 'GuestPassword' in request.form :
        username = request.form['GuestUsername']
        password = request.form['GuestPassword']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM msguest WHERE GuestName = %s AND GuestPass = %s",(username, password,))
        user = cur.fetchone()

        if user:
            session['loggedin'] = True
            session['id'] = user['GuestID']
            session['username'] = user['GuestName']
            cur.close()
            return redirect(url_for('home'))
        else:
            text = 'incorrect username/password!'
    elif request.method == 'POST':
        text = "Fill in the forms"

    return render_template('userLogin.html', msg=text)

@app.route('/login/admin', methods=['GET', 'POST'])
def adminLogin():
    text = ''
    if request.method == 'POST' and 'StaffUsername' in request.form and 'StaffPassword' in request.form :
        username = request.form['StaffUsername']
        password = request.form['StaffPassword']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM msstaff WHERE StaffName = %s AND StaffPass = %s",(username, password,))
        user = cur.fetchone()

        if user:
            session['loggedinn'] = True
            session['id'] = user['StaffID']
            session['username'] = user['StaffName']

            conn = mysql.connect()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM msreservation")
            data = cur.fetchall()
            cur.close

            return redirect(url_for('adminHome'))
        else:
            text = 'incorrect username/password!'
    elif request.method == 'POST':
        text = "Fill in the forms"

    return render_template('adminLogin.html', msg=text)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('loggedinn', None)
    session.pop('id', None)
    session.pop('username', None)

    return redirect(url_for('home'))

@app.route('/register', methods=['GET','POST'])
def register():
    text = ''
    if request.method == 'POST' and 'GuestUsername' in request.form and 'GuestEmail' in request.form and 'GuestPhone' in request.form and 'GuestPassword' in request.form and 'GuestGender' in request.form:
        username = request.form['GuestUsername']
        email = request.form['GuestEmail']
        phone = request.form['GuestPhone']
        password = request.form['GuestPassword']
        gender = request.form['GuestGender']

        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(" SELECT * FROM msguest WHERE GuestName = %s OR Email = %s",(username,email,))
        accounts = cur.fetchone()

        if accounts:
            text = "Account already exists"
        else:
            cur.execute("INSERT INTO msguest VALUES(NULL, %s, %s, %s, %s, %s)", (username, password, phone, gender, email,))
            conn.commit()
            text = "Account successfully created!"    
    elif request.method=='POST':
        text = "Fill in the forms"
    return render_template('register.html',text=text)

if __name__ == '__main__':
    app.run(debug = True)