import sqlite3
import os
import model


INDOORENV_TABLE = "indoorEnvironment"
COMMAND_TABLE = "command"
DB_PATH = "***********"

class SqlHandler:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()

    def insert_indoorEnv_column(self, column):
        try:
            self.cur.execute('INSERT INTO ' + INDOORENV_TABLE +' VALUES (?, ?, ?)', (column.temp, temp.hum, temp.press))
        
        except sqlite3.Error as e:
            print(e)

        conn.commit()
    
    def insert_command_column(self, column):
        try:
            self.cur.execute('INSERT INTO ' + COMMAND_TABLE + ' VALUES (?, ?, ?, ?, ?)', (column.power, column.mode, column.temp, column.swing, column.fan))
        
        except sqlite3.Error as e:
            print(e)

        conn.commit()
    
    def delete_column(self, table_name, id):
        try:
            self.cur.execute('DELETE FROM ' + table_name + ' WHERE id = ?', (id))

        except sqlite3.Error as e:
            print(e)

        conn.commit()

    def get_column(self, table_name, id):
        try:
            self.cur.execute('SELECT * FROM ' + table_name + ' WHERE id=?', (id))

        except sqlite3.Error as e:
            print(e)

        column = self.cur.fetchall()
        
        return column
    
    def get_latest_id(self, table_name):
        try:
            self.cur.execute('SELECT id FORM ' + table_name)
        
        except sqlite3.Error as e:
            print(e)

        id_row = self.cur.fetchall() 
   
        return max(id_row)
    
    def get_latest_indoorEnv(self):
        try:
            id = get_latest_id(get_latest_id(INDOORENV_TABLE))
            indoorEnv_column = get_column(INDOORENV_TABLE, id)
            indoorEnv = model.IndoorEnv(indoorEnv_column)
        except sqlite3.Error as e:
            print(e)
        
        return indoorEnv
    
    
    def get_latest_commnad(self):
        try:
            id = get_latest_id(get_latest_id(COMMAND_TABLE))
            command_column = get_column(COMMAND_TABLE, id)
            command = model.AirConCommnad(command_column)
        except sqlite3.Error as e:
            print(e)

        return command
    
