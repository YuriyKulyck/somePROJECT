import DBmanager

dbmanager = DBmanager.DBManager("db_name.sql")
dbmanager.create_tables()

dbmanager.add_catalog(2, "Каталог побутової техніки", "Новорічні знижки для сімейних свят! -70%!!! ")