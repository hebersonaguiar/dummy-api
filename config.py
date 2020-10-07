from app import app
from flask_mysqldb import MySQL

mysql = MySQL()
app.config['MYSQL_USER'] = 'USER_MYSQL'
app.config['MYSQL_PASSWORD'] = 'PASS_MYSQL'
app.config['MYSQL_DB'] = 'DB_MYSQL'
app.config['MYSQL_HOST'] = 'HOST_MYSQL'
mysql.init_app(app)