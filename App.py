from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "flash message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'collegestudents'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("select * from students")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template('index.html', data=fetchdata)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Added Sucessfully")
        fname = request.form['fname']
        lname = request.form['lname']
        cname = request.form['cname']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (fname,lname,cname) VALUES (%s,%s,%s)", (fname, lname, cname))
        mysql.connection.commit()
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
