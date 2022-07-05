import sqlite3


def add_date_sql(id_sql, name, str_text, date):
    sql = sqlite3.connect('database.db')
    cursor = sql.cursor()
    sql_table_avito ="""CREATE TABLE IF NOT EXISTS avito(
    id integer PRIMARY KEY,
    name_ text NOT NULL,
    str_text text,
    date_ text NOT NULL
    );"""
    cursor.execute(sql_table_avito)
    sql_date_insert = """INSERT INTO avito VALUES (?, ?, ?, ?);"""
    data_sql = id_sql, name, str_text, date
    cursor.execute(sql_date_insert, data_sql)
    sql.commit()
    cursor.close()
    sql.close()
