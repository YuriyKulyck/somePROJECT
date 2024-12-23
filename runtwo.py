import DBmanager

dbmanager = DBmanager.DBManager("db_name.sql")
dbmanager.create_tables()

dbmanager.add_catalog(6, "Охолоджені та розливні напої", "Доставляються 24/7 з 100% цілісністю!")