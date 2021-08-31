import sqlite3


DB_PATH = 'test.sqlite'

class sqlite_handller(object):
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()

def init(handller):
   handller.cur.execute('CREATE TABLE indoorEnviroment(id integer primary key, temp, text, hum text, press text)')
   handller.conn.commit()
   handller.cur.execute('CREATE TABLE command(id integer primary key, power text, mode text, temp text, swing text, fan text)')
   handller.conn.commit()

def main():
    handller = sqlite_handller()
    init(handller)

if __name__ == '__main__':
    main()
