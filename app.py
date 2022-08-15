from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
import json
import os
import base64

mysql = MySQL()
app = Flask(__name__)

dbuser = os.environ.get('DBUSER')
dbpass = os.environ.get('DBPASSWORD')

# def stringToBase64(s):

def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')


dbuser=stringToBase64(dbuser)
dbpass=stringToBase64(dbpass)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = base64ToString(dbuser)
app.config['MYSQL_DATABASE_PASSWORD'] = base64ToString(dbpass)
app.config['MYSQL_DATABASE_DB'] = os.environ.get('DBSELECT')
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('DBHOST')
mysql.init_app(app)

@app.route("/")
def hello():
    return render_template(os.environ.get('DEPLOY_INDEX'))

@app.route('/showSignUp')
def showSignUp():
    return render_template(os.environ.get('DEPLOY_SIGNUP'))

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call MySQL
            
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_createUser',(_name,_email,_password))
            data = cursor.fetchall()

            if len(data) == 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=5000)