#!/usr/bin/python3
# -*- coding: utf-8 -*-
from configparser import ConfigParser
from os import path, listdir
from settings.utils import find_ext_file, basepath


settings = dict()
APP_PATH = path.dirname(path.dirname(path.abspath(__file__)))
ROOT_PATH = path.dirname(APP_PATH)

settings['config.file.main'] = basepath('config', 'main.ini')
config = ConfigParser(allow_no_value=True)
config.read((settings['config.file.main'],))
DB_CRED = False
try:
    settings['db_host'] = config.get('DB_ROOT', 'host')
    settings['db_port'] = config.get('DB_ROOT', 'port')
    settings['db_user'] = config.get('DB_ROOT', 'user')
    settings['db_pass'] = config.get('DB_ROOT', 'pass')
    settings['db_dbname'] = config.get('DB_ROOT', 'dbname')

    settings['db_app_host'] = config.get('DB_APP', 'host')
    settings['db_app_port'] = config.get('DB_APP', 'port')
    settings['db_app_user'] = config.get('DB_APP', 'user')
    settings['db_app_pass'] = config.get('DB_APP', 'pass')
    settings['db_app_dbname'] = config.get('DB_APP', 'dbname')
    DB_CRED = True
except Exception as e:
    pass

CONFIG_JSON_PATHS = find_ext_file("json", APP_PATH + "/config")
GOOGLE_API_CRED = False
if len(CONFIG_JSON_PATHS) > 0:
    GOOGLE_JSON_KEY = CONFIG_JSON_PATHS[0]
    GOOGLE_API_CRED = True
# based by https://stackoverflow.com/a/3964691/6362121
