import sqlite3


def connect_db(func):
    """Decorator for create, commit and close a db connection"""
    def inner_function(DATABASE="workzydata.db", *args, **kwargs):
        db_func = None
        try:
            conn = sqlite3.connect(DATABASE)
            db_func = func(conn, *args, **kwargs)
        except sqlite3.Error as err:
            print("An error occurred", err.args[0])
        else:
            conn.commit()
        finally:
            conn.close()
        return db_func

    return inner_function


@connect_db
def create_table(conn):
    """DB method for create a jobs table"""
    conn.execute("""
    CREATE TABLE jobs (date text, workspace text, minutes integer)
    """)


@connect_db
def insert(conn, workspace):
    """DB method for insert a new workspace history"""
    c = conn.cursor()
    c.execute("""
    INSERT INTO jobs (date, workspace, minutes) VALUES (?,?,?)
    """, (workspace.date(), workspace.name, workspace.minutes))


@connect_db
def select(conn, workspace):
    """DB method to retrieve a workspace history"""
    c = conn.cursor()
    c.execute("SELECT * FROM jobs WHERE workspace=?", (workspace.name,))
    print(c.fetchone())
