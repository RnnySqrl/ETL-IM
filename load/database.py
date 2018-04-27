#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql
from settings.settings import settings

class DataBase(object):
    def __init__(self):
        config_db = {
            'user': settings['db_user'],
            'password': settings['db_pass'],
            'host': settings['db_host'],
            'database': settings['db_dbname'],
            'port': int(settings['db_port'])
        }
        self._conn_db = pymysql.connect(**config_db)
        self._cursor_db = self._conn_db.cursor(
            pymysql.cursors.DictCursor
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._cursor_db.close()
        self._conn_db.close()

    def insert_data(self, query):
        try:
            self._cursor_db.execute(query)
            self._conn_db.commit()
            print(str(self._cursor_db.rowcount) + " rows inserted correctly")
        except pymysql.Error as e:
            self._conn_db.rollback()
            print(e)
            print("Couldn't insert values")




class ViewerDataBase(object):

    def __init__(self):

        config_app_db = {
            'user': settings['db_app_user'],
            'password': settings['db_app_pass'],
            'host': settings['db_app_host'],
            'database': settings['db_app_dbname'],
            'port': int(settings['db_app_port'])
        }
        self._conn_app_db = pymysql.connect(**config_app_db)
        self._cursor_app_db = self._conn_app_db.cursor(
            pymysql.cursors.DictCursor
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._cursor_app_db.close()
        self._conn_app_db.close()

    def query_data_state(self, state: str):
        countries = [
            country['country']
            for country in self.__countries_state(state)
            if country['country']
        ]
        if len(countries) <= 0:
            print(
                "State: {0} doesn't exists or we haven't got data"
                .format(state)
            )
            return None
        elif len(countries) == 1:
            chosen_country = countries[0]
        else:
            # https://stackoverflow.com/a/954840/6362121
            chosen_country = input(
                "The state {0} is in {1} countries please chose the country"
                    .format(
                    state,
                    ",".join(countries)
                     + " you want: "
                )
            ).upper()
            print(chosen_country)
            if chosen_country not in countries:
                print("the country you have selected is not in the options")
                return None

        query = """
            SELECT
                *
            FROM
                daily_temperature_90_00
            WHERE
                STATE = {0} AND country = {1}
            ORDER BY `date`
        """.format(
            "'" + state + "'",
            "'" + chosen_country + "'"
        )
        try:
            self._cursor_app_db.execute(query)
            return self._cursor_app_db.fetchall()
        except pymysql.Error as e:
            print(e)
            return []

    def __countries_state(self, country: str):
        query = """
        SELECT DISTINCT
          country
        FROM
            daily_temperature_90_00
        WHERE
            state = {0}
        """.format("'" + country + "'")
        try:
            self._cursor_app_db.execute(query)
            return self._cursor_app_db.fetchall()
        except pymysql.Error as e:
            print(e)
            return []
