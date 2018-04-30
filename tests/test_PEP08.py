import pycodestyle
from settings.utils import find_ext_file
from settings.settings import APP_PATH


def test_code_format():
    """Test that we conform to PEP-8."""
    style = pycodestyle.StyleGuide()
    all_files = find_ext_file("py", APP_PATH)
    all_files += find_ext_file("py", APP_PATH + "/googleBigQuery")
    all_files += find_ext_file("py", APP_PATH + "/load")
    all_files += find_ext_file("py", APP_PATH + "/settings")
    all_files += find_ext_file("py", APP_PATH + "/tests")
    result = style.check_files(all_files)
    assert result.file_errors == 0
