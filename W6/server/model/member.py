import db.db as db


def get_all_member():
    db.get_connection()

    cursor = db.get_cursor()
    cursor.execute("SELECT name, username, password FROM member")
    res = cursor.fetchall()

    db.close_cursor()
    db.close_connection()
    return res


def check_and_add_membership(name, account, password):
    db.get_connection()
    cursor = db.get_cursor()

    sql_cmd = '''
        SELECT name, username, password  
        FROM member 
        WHERE username=%(username)s;
    '''
    sql_content = {
        "username": account
    }

    cursor.execute(sql_cmd, sql_content)
    res = cursor.fetchone()

    if res is None:
        add_membership(name, account, password)
        return False

    db.close_cursor()
    db.close_connection()
    return res


def add_membership(name, account, password):
    db.get_connection()
    cursor = db.get_cursor()

    sql_cmd = '''
        INSERT INTO member (name, username, password) 
                    values (%(name)s, %(username)s, %(password)s);
    '''
    sql_content = {
        "name": name,
        "username": account,
        "password": password
    }

    try:
        cursor.execute(sql_cmd, sql_content)
    except Exception as err:
        print("Failed to insert values %s, %s, %s", name, account, password)
    finally:
        db.commit()
        db.close_cursor()
        db.close_connection()

    print("Successfully insert values %s, %s, %s", name, account, password)

    return affected_count
