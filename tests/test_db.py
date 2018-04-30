from load.database import DataBase, ViewerDataBase
import pytest
from settings.settings import DB_CRED


# Tests to verify the connection with our database is established
@pytest.mark.skipif(not DB_CRED, reason="Credentials not iniciated")
def test_conn_root_db():
    assert DataBase()


@pytest.mark.skipif(not DB_CRED, reason="Credentials not iniciated")
def test_conn_app_db():
    assert ViewerDataBase()
