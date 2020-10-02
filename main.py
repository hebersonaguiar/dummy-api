import pymysql, json, re
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
		
@app.route('/add', methods=['POST'])
def add_emp():
    try:
        _json = request.json
        # _name = _json['name']
        # _email = _json['email']
        # _phone = _json['phone']
        # _address = _json['address']
        name = str(request.json.get('name', None))
        email = str(request.json.get('email', None))
        phone = str(request.json.get('phone', None))
        address = str(request.json.get('address', None))
        print(type(name))
        print("Before IF")
        print("Name: " + name + " Phone: " + phone + " Address: " + address + " Request: " + request.method)
        # if _name and _email and _phone and _address and request.method == 'POST':
        if name and email and phone and address and request.method == 'POST': 
            print("After IF")
            print("Name: " + name + " Phone: " + phone + " Address: " + address + " Request: " + request.method)
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO rest_emp (name, email, phone, address) VALUES (%s, %s, %s, %s)", (name, email, phone, address))
            # sqlQuery = "INSERT INTO rest_emp(name, email, phone, address) VALUES(%s, %s, %s, %s)", (_name, _email, _phone, _address)
            # bindData = (_name, _email, _phone, _address)            
            # cursor = conn.cursor()
            # cur.execute(sqlQuery)
            mysql.connection.commit()
            #respone = jsonify('Employee added successfully!')
            respone = 'Employee added successfully!'
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cur.close()

@app.route('/emp')
def emp():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, name, email, phone, address FROM rest_emp")
        empRows = cur.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cur.close()
        
@app.route('/emp/<int:id>')
def emp_id(id):
    try:
        cur = mysql.connection.cursor()
        # cursor = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT id, name, email, phone, address FROM rest_emp WHERE id =%s", id)
        empRow = cur.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cur.close()

@app.route('/update', methods=['PUT'])
def update_emp():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']
        if _name and _email and _phone and _address and _id and request.method == 'PUT':
            sqlQuery = "UPDATE rest_emp SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
            bindData = (_name, _email, _phone, _address, _id,)
            cur = mysql.connection.cursor()
            # cursor = conn.cursor()
            cur.execute(sqlQuery, bindData)
            mysql.connection.commit()
            respone = jsonify('Employee updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_emp(id):
    try:
        cur = mysql.connection.cursor()
        # cursor = conn.cursor()
        cur.execute("DELETE FROM rest_emp WHERE id =%s", (id,))
        mysql.connection.commit()
        respone = jsonify('Employee deleted successfully!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cur.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
        }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')