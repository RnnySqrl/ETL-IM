from load.database import DataBase, ViewerDataBase


# Tests to verify the connection with our database is established
def test_conn_root_db():
    assert DataBase()

def test_conn_app_db():
    assert ViewerDataBase()
