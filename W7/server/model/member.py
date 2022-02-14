import db.db as db


def get_all_member() -> list:
    with db.DB() as _db:
        sql_cmd = "SELECT name, username, password FROM member"
        res = _db.fetch_db(sql_cmd=sql_cmd, is_fetch_one=False)
    return res


def get_member(account, password) -> tuple or None:

    sql_cmd = '''
        SELECT name, username, password  
        FROM member 
        WHERE username=%(username)s and password=%(password)s;
    '''
    sql_content = {
        "username": account,
        "password": password
    }

    with db.DB() as _db:
        res = _db.fetch_db(sql_cmd, sql_content)
    return tuple(next(iter(res)))


def query_membership(account) -> tuple or None:

    sql_cmd = '''
        SELECT id, name, username
        FROM member
        WHERE username=%(username)s;
    '''
    sql_content = {
        "username": account,
    }

    with db.DB() as _db:
        res = _db.fetch_db(sql_cmd, sql_content)
    return tuple(next(iter(res))) if next(iter(res)) else None


def check_and_add_membership(name, account, password) -> bool:

    sql_cmd = '''
        SELECT name, username, password  
        FROM member 
        WHERE username=%(username)s;
    '''
    sql_content = {
        "username": account,
    }

    with db.DB() as _db:
        res = _db.fetch_db(sql_cmd, sql_content)

    if next(iter(res)) is None:
        add_membership(name, account, password)
        return False

    return True


def add_membership(name, account, password) -> int:

    sql_cmd = '''
        INSERT INTO member (name, username, password) 
                    values (%(name)s, %(username)s, %(password)s);
    '''
    sql_content = {
        "name": name,
        "username": account,
        "password": password
    }

    with db.DB() as _db:
        affected_rows = _db.crud(sql_cmd, sql_content)

        if affected_rows > 0:
            print(
                f"Successfully add {affected_rows} membership", name, account, password)

    return affected_rows


def update_membership_name(name, username) -> int:

    sql_cmd = '''
        UPDATE member 
        SET name = %(name)s 
        WHERE username = %(username)s;
    '''
    sql_content = {
        "name": name,
        "username": username,
    }

    with db.DB() as _db:
        affected_rows = _db.crud(sql_cmd, sql_content)

        if affected_rows > 0:
            print(
                f"Successfully update {affected_rows} membership's name", name, username)

    return affected_rows
