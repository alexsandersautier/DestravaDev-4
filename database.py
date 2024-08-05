import sqlite3
from datetime import datetime

class Connection():
    database_name = 'tasks.db'
    con = None
    table = '''
        CREATE TABLE tasks(
            id INTEGER PRIMARY KEY,
            description TEXT,
            finished BOOLEAN,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''

    def __init__(self):
        try:
            self.connect()
        except Exception as e: 
            print(e)
        try:    
            self.create_table()
        except:
            ...

    def connect(self):
        self.con = sqlite3.connect(self.database_name)
        return self.con.cursor()
    

    def create_table(self):
        self.con.execute(self.table)

    def create(self, description):
        sql = f'''
            INSERT INTO tasks(description, finished, created_at, updated_at)
            VALUES('{description}', {False}, '{datetime.now()}', '{datetime.now()}') 
        '''
        self.con.execute(sql)
        self.con.commit()
    
    def update(self, id, description, finished = False):
        task = self.select_by_id(id)
        aux = description if description != '' else task[1]
        sql = f'''
            UPDATE tasks SET description = '{aux}', finished = {finished}, updated_at = '{datetime.now()}'
            WHERE id = {id}
        '''
        self.con.execute(sql)
        self.con.commit()
    
    def select_all(self):
        registers = self.con.execute('SELECT * FROM tasks')
        return registers.fetchall()

    def select_by_id(self, id):
        register = self.con.execute(f'SELECT * FROM tasks WHERE id = {id}')
        return register.fetchone()
    
    def delete(self, id):
        self.con.execute(f'DELETE FROM tasks WHERE id = {id}')
        self.con.commit()
