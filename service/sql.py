import sqlite3
import os


INDOORENV_TABLE = "indoorEnvironment_table"
COMMAND_TABLE = "command_tablen"

class SqlHandler:
    def __init__(self):
        self.conn = sqlite3.connect(os.getenv['DB_PATH'])
        self.cur = self.conn.cursor()

    def insert_column(self, table_name, column):
        cur.execute('INSERT INTO ? VALUES (?, ?, ?)', [column])
        conn.commit()
    
    def delete_column(self, table_name, id):
        cur.execute('DELETE FROM ? WHERE id = ?', [table_name, id])
        conn.commit()
    
    def get_column(self, table_name, id):
        cur.execute('SELECT * FROM ' + table_name)

    
    def get_latest_id(self, table_name):
        cur.execute('SELECT id FORM ' + table_name)
        id~_row = cur.fetchall()
        return max(id_row)
    
    def get_latest_indoorEnv(self):
        id = get_latest_id(self)
    
    
    def get_latest_commnad(self):
        id = get_latest_id(self)
    
