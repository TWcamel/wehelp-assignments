import mysql.connector
from mysql.connector import errorcode


CONFIG = {
    'user': 'scott',
    'password': 'password',
    'host': 'db',
    'database': 'your_db',
    'raise_on_warnings': True
}


def get_connection():
    global cnx
    try:
        cnx = mysql.connector.connect(**CONFIG)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def close_connection():
    try:
        cnx.close()
    except Exception as err:
        print(err)


def check_connection():
    if cnx.is_closed():
        return print("Flask is disconnect to MySql")
    else:
        return print("Flask is connect to MySql")


def get_cursor():
    try:
        return cnx.cursor()
    except Exception as err:
        print(err)


def close_cursor():
    try:
        cnx.cursor().close()
    except Exception as err:
        print(err)


def commit():
    try:
        cnx.commit()
    except Exception as err:
        print(err)

if __name__ == "__main__":
    get_connection()

