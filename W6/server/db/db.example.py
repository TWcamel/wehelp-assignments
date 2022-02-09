import mysql.connector
from mysql.connector import errorcode


CONFIG = {
    'user': 'scott',
    'password': 'password',
    'host': 'db',
    'database': 'db',
    'raise_on_warnings': True
}


def run_db():
    try:
        cnx = mysql.connector.connect(**CONFIG)
        print("If Flask is connect to MySql?", cnx.is_connected())
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


if __name__ == "__main__":
    run_db()
