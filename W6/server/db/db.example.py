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
    try:
        cnx = mysql.connector.connect(**CONFIG)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return cnx


def db_fetch_all(sql_cmd):
    cnx = get_connection()
    cursor = cnx.cursor()
    try:
        cursor.execute(sql_cmd)
        print("Database query successfully")
    except Exception as err:
        print("Failed to query database")
    finally:
        res = cursor.fetchall()
        cursor.close()
        cnx.close()
    return res


def db_fetch_one(sql_cmd, sql_content):
    cnx = get_connection()
    cursor = cnx.cursor()
    try:
        cursor.execute(sql_cmd, sql_content)
        print("Database query successfully")
    except Exception as err:
        print("Failed to query database")
    finally:
        res = cursor.fetchone()
        cursor.close()
        cnx.close()
    return res


def db_crud(sql_cmd, sql_content):
    cnx = get_connection()
    cursor = cnx.cursor()
    try:
        cursor.execute(sql_cmd, sql_content)
    except Exception as err:
        print("Failed to do CRUD operation")
        return False
    finally:
        cnx.commit()
        cursor.close()
        cnx.close()
    return True

