from flask import Flask, render_template, url_for, request
# from flask.mysqldb import MySQL
import datetime
# import pymsql.cursors

app = Flask(__name__)

# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['MYSQL_DATABASE_DB'] = 'dictionary'
# app.config['MYSQL_DATABASE_USER'] = 'user'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'

# mysql = MySQL(app, cursorclass=mysql.cursors.DictCursor)

@app.route('/', methods= ['GET', 'POST'])
def index():
    user_response = ''
    # if request.method == 'POST':
    #     user_input = request.form['word']
    #     conn = mysql.get_id()
    #     cur = conn.cursor()
    #     cur.execute('select meaning from word where word=%s', (user_input))
    #     rv = cur.fetchall()
    #     if(len(rv) > 0):
    #         user_response = rv[0]['meaning']
    #     else:
    #         user_response = 'Word not found'
    return render_template('index.html', user_response = user_response)

@app.route('/dashboard')
def dashboard():
    rv=''
    #     conn = mysql.get_id()
    #     cur = conn.cursor()
    #     cur.execute('select * from word)
    #     rv = cur.fetchall()
    #     for item in rv:
    #       print(item)        
    return render_template('dashboard.html', words=rv)


if __name__ == "__main__":
    app.run(debug=True)