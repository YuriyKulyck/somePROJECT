import sqlite3
class DBManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)


    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS catalog(
            "id"  INT PRIMARY KEY,
            "Title"	varchar(255),
            "Description" TEXT
            );
            """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Article(
            "id_of_article"	INT PRIMARY KEY,
            "id_catalog"	varchar(255),
            "Content" TEXT,
            "description" TEXT,
            "Price" TEXT,
            "Look" TEXT,
            "Connections" TEXT,
            "Location" TEXT,
            "Properties_and_signs" TEXT
            );
            """)
        self.connection.commit()

    def add_catalog(self, id, title, description):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO catalog(id, Title, Description) VALUES (?, ?, ?)", [id, title, description])
        self.connection.commit()
        cursor.close()

    def add_article(self, id_of_article, id_catalog, Content, description, Price, Look, Connections, Location, Properties_and_signs):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Article(id_of_article, id_catalog, Content, description, Price, Look, Connections, Location, Properties_and_signs)) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", [id_of_article, id_catalog, Content, description, Price, Look, Connections, Location, Properties_and_signs])
        self.connection.commit()
        cursor.close()