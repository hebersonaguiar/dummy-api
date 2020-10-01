from app import app
#from flaskext.mysql import MySQL
from flask_mysqldb import MySQL

mysql = MySQL()
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'my-secret-pw'
app.config['MYSQL_DB'] = 'rest_emp'
app.config['MYSQL_HOST'] = 'mysql'
mysql.init_app(app)