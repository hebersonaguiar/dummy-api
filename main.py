import json, re, csv
from app import app
from config import mysql
from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_jsonpify import jsonify
from json import dumps
from io import StringIO

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
		return 'error'
	finally:
		cur.close()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')