import sqlite3
import os
from ..model import airconcommand
from ..model import indoorenvironment


INDOORENV_TABLE = "indoorEnvironment_table"
COMMAND_TABLE = "command_table"
DB_PATH = "**********"

class SqlHandler:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()

    def insert_indoorEnv_column(self, column):
        cur.execute('INSERT INTO ? VALUES (?, ?, ?)', [INDOORENV_TABLE, column.temp, temp.hum, temp.press])
        conn.commit()
        
        return get_latest_id(table_name)
    
    def insert_command_column(self, column):
        cur.execute('INSERT INTO ? VALUES (?, ?, ?, ?, ?)', [COMMAND_TABLE, column.power, column.mode, column.temp, column.swing, column.fan])
        conn.commit()
        
        return get_latest_id(table_name)
    
    def delete_column(self, table_name, id):
        cur.execute('DELETE FROM ? WHERE id = ?', [table_name, id])
        conn.commit()

        return get_latest_id(table_name)

    def get_column(self, table_name, id):
        cur.execute('SELECT * FROM ' + table_name)
        column = cur.fetchall()

        return column
    
    def get_latest_id(self, table_name):
        cur.execute('SELECT id FORM ' + table_name)
        id_row = cur.fetchall() 
        return max(id_row)
    
    def get_latest_indoorEnv(self):
        id = get_latest_id(self)
        indoorEnv_column = get_column(INDOORENV_TABLE, id)
        indoorEnv = indoorenvironment.IndoorEnv(indoorEnv_column)
        
        return indoorEnv
    
    
    def get_latest_commnad(self):
        id = get_latest_id(self)
        command_column = get_column(COMMAND_TABLE, id)
        command = airconcommand.AirConCommnad(command_column)

        return command
    
