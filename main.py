import json, re, csv
# from app import app
# from config import mysql
from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_jsonpify import jsonify
from json import dumps
from io import StringIO

# app = Flask(__name__)
# api = Api(app)
# CORS(app, resources={r"/*": {"origins": "*"}})
# app.secret_key = "flash message"

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "flash message"

# mysql = MySQL()
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'my-secret-pw'
app.config['MYSQL_DB'] = 'rest_emp'
app.config['MYSQL_HOST'] = 'mysql'
# mysql.init_app(app)

mysql = MySQL(app)


@app.route('/add', methods=['POST'])
def add_emp():
    try:
        name = str(request.json.get('name', None))
        email = str(request.json.get('email', None))
        phone = str(request.json.get('phone', None))
        address = str(request.json.get('address', None))
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO rest_emp (name, email, phone, address) VALUES (%s, %s, %s, %s)", (name, email, phone, address))
        mysql.connection.commit()
        
        return 'Usuario Inserido'
    except Exception as e:
        print(e)
    finally:
        cur.close()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')