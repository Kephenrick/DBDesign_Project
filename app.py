from flask import Flask, render_template, session, request, redirect, url_for
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors

mysql = MySQL()
app = Flask(__name__, template_folder='templates')
app.secret_key = 'secretkey'

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'databasehotel'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/', methods=['GET'])
def home():
    if 'loggedin' in session:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM msreservation WHERE GuestID=%s", session['id'])
        data = cur.fetchall()
        cur.close()
        return render_template('index.html', reservations=data)

    return render_template('index.html')

@app.route('/adminPage', methods=['GET'])
def adminHome():
    if 'loggedin' in session:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM msreservation")
        data = cur.fetchall()
        cur.close
        return render_template('adminPage.html', reservations=data)

    return render_template('adminPage.html')

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

@app.route('/delete/<int:id>')
def deleteBooking(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("DELETE FROM msreservation WHERE ReservationID = %s", id)
    conn.commit()
    text = 'data deleted successfully'

    return render_template('index.html', deletemsg=text)

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
            session['loggedin'] = True
            session['id'] = user['StaffID']
            session['username'] = user['StaffName']
            cur.close()
            return redirect(url_for('adminHome'))
        else:
            text = 'incorrect username/password!'
    elif request.method == 'POST':
        text = "Fill in the forms"

    return render_template('adminLogin.html', msg=text)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)