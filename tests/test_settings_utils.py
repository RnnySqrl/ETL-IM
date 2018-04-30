from settings.utils import find_ext_file
from settings.settings import APP_PATH


def test_find_ext_file():
    assert find_ext_file("sql", APP_PATH + "/tests/data")
