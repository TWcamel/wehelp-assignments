import db.db as db


def get_all_member():
    return db.db_fetch_all(sql_cmd="SELECT name, username, password FROM member")


def get_member(account, password):

    sql_cmd = '''
        SELECT name, username, password  
        FROM member 
        WHERE username=%(username)s and password=%(password)s;
    '''
    sql_content = {
        "username": account,
        "password": password
    }

    return db.db_fetch_one(sql_cmd, sql_content)


def check_and_add_membership(name, account, password):

    sql_cmd = '''
        SELECT name, username, password  
        FROM member 
        WHERE username=%(username)s;
    '''
    sql_content = {
        "username": account,
    }

    res = db.db_fetch_one(sql_cmd, sql_content)

    if res is None:
        add_membership(name, account, password)
        return False

    return res


def add_membership(name, account, password):

    sql_cmd = '''
        INSERT INTO member (name, username, password) 
                    values (%(name)s, %(username)s, %(password)s);
    '''
    sql_content = {
        "name": name,
        "username": account,
        "password": password
    }

    if db.db_crud(sql_cmd, sql_content):
        print("Successfully add membership", name, account, password)
