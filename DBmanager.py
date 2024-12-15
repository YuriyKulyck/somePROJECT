import sqlite3
class DBManager:
    def __init__(self):
        self.connection = sqlite3.connect()


    def create_tables(self):
        pass