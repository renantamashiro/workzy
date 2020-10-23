import sqlite3


def connect_with_db(func):
    def inner_function(*args, **kwargs):
        conn = sqlite3.connect("example.db")  # db name change that
        return func(conn, *args, **kwargs)

    return inner_function


@connect_with_db
def insert_db(conn, name, another):
    conn.execute("INSERT INTO test VALUES (?,?)", (name, another))
    conn.commit()


# inserir tratamento de exceção no decorator


def create_table_workspace(workspace):
    pass


def insert():
    pass


# tabela de workspaces (chave e nome do workspace)
# tabela processos (chave workspace, chave processo e nome do processo)
# tabela de lançamento de tempo em workspace
# (chave workspace, data, minutos trabalhados)
