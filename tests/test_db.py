from load.database import DataBase, ViewerDataBase

def test_conn_root_db():
    assert DataBase()

def test_conn_app_db():
    assert ViewerDataBase()

