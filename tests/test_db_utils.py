from load import utils
import json


def test_to_date1():
    assert utils.__to_date(5, 12, 1994) == "1994-12-05"


def test_to_date2():
    assert utils.__to_date("3", None, -1) == "0000-00-00"


def test_format_query_values():
    data_file_test = json.load(open("tests/data/data_mock.json"))
    file_result = open("tests/data/query_values.txt")
    string_result = file_result.read()
    assert utils.__format_query_values(data_file_test['data']) == string_result


def test_generate_query_data():
    data_file_test = json.load(open("tests/data/data_mock.json"))
    file_result = open("tests/data/result_query.sql")
    string_result = file_result.read()
    assert utils.generate_query_data(data_file_test['data']) == string_result
