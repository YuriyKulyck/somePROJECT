import DBmanager

dbmanager = DBmanager.DBManager("db_name.sql")
dbmanager.create_tables()

dbmanager.add_catalog(7, "Дитячі товари", "Знижки на дитячі іграшки та засоби -65%!")