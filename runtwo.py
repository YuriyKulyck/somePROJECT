import DBmanager

dbmanager = DBmanager.DBManager("db_name.sql")
dbmanager.create_tables()

dbmanager.add_catalog(8, "Одяг та взуття", "Знижка на вироби Nike до 87%!")