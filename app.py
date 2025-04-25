from flask import Flask, render_template, session, request, redirect, url_for
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors
import sqlite3

mysql = MySQL()
app = Flask(__name__, template_folder='templates')
app.secret_key = 'secretkey'

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'dbdesign2'
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

@app.route('/adminPage', methods=['GET'])
def adminHome():
    if 'loggedin' in session:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM msreservation")
        data = cur.fetchall()
        cur.close

    return render_template('adminPage.html', reservations=data)

@app.route('/login', methods=['GET', 'POST'])
def userLogin():
    text = ''
    if request.method == 'POST' and 'GuestUsername' in request.form and 'GuestPassword' in request.form :
        username = request.form['GuestUsername']
        password = request.form['GuestPassword']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM msguest WHERE GuestUsername = %s AND GuestPassword = %s",(username, password,))
        user = cur.fetchone()

        if user:
            session['loggedin'] = True
            session['id'] = user['GuestID']
            session['username'] = user['GuestUsername']
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
        cur.execute("SELECT * FROM msstaff WHERE StaffUsername = %s AND StaffPassword = %s",(username, password,))
        user = cur.fetchone()

        if user:
            session['loggedin'] = True
            session['id'] = user['StaffID']
            session['username'] = user['StaffUsername']
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

@app.route('/register', methods=['GET','POST'])
def register():
    text = ''
    if request.method == 'POST' and 'username' in request.form and 'email' in request.form and 'password' in request.form:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(" SELECT * FROM accounts WHERE username = %s OR email = %s",(username,email,))
        accounts = cur.fetchone()

        if accounts:
            text = "Account already exists"
        else:
            cur.execute("INSERT INTO accounts VALUES(NULL, %s, %s, %s)", (username, email, password,))
            conn.commit()
            text = "Account successfully created!"    
    elif request.method=='POST':
        text = "Fill in the forms"
    return render_template('register.html',text=text)

if __name__ == '__main__':
    app.run(debug = True)