#!/bin/bash

set -e

help() {
    echo "Usage: docker run -dti --link mysql:mysql --name dummy-api -e MYSQL_HOST=[value] -e MYSQL_USER=[value] -e MYSQL_PASS=[value] -e MYSQL_DB=[value]  image:tag" >&2
    echo
    echo "   MYSQL_HOST          hostname mysql database"
    echo "   MYSQL_USER          user for connecting the mysql database"
    echo "   MYSQL_PASS          passowrd of user for connecting the database"
    echo "   MYSQL_DB            name database for connect "
    echo
    exit 1
}

if [ ! -z "$MYSQL_HOST" ] || [ ! -z "$MYSQL_USER" ] || [ ! -z "$MYSQL_PASS" ]|| [ ! -z "$MYSQL_DB" ]; then


    sed -i "s/MYSQL_HOST/$MYSQL_HOST/g" /opt/config.py
    sed -i "s/MYSQL_USER/$MYSQL_USER/g" /opt/config.py
    sed -i "s/MYSQL_PASS/$MYSQL_PASS/g" /opt/config.py
    sed -i "s/MYSQL_DB/$MYSQL_DB/g" /opt/config.py  

else
	echo "Please enter the required data!"
	help
fi

exec "$@"