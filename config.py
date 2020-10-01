from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'my-secret-pw'
app.config['MYSQL_DATABASE_DB'] = 'rest_emp'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
mysql.init_app(app)