from app import app
from flask_mysqldb import MySQL

mysql = MySQL()
app.config['MYSQL_USER'] = 'MYSQL_USER'
app.config['MYSQL_PASSWORD'] = 'MYSQL_PASSWORD'
app.config['MYSQL_DB'] = 'MYSQL_DB'
app.config['MYSQL_HOST'] = 'MYSQL_HOST'
mysql.init_app(app)