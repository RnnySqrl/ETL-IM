#!/usr/bin/python3
# -*- coding: utf-8 -*-
from google.cloud import bigquery
import os
from settings.settings import GOOGLE_JSON_KEY


class NOAA_GSOD(object):

    def __init__(self):
        # https://stackoverflow.com/a/1506046/6362121
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_JSON_KEY

        self.client = bigquery.Client()

    def get_data(self):
        query = """
                SELECT
                ROUND((MAX(max)-32)*5/9,1) as celsius_max,
                ROUND((MIN(min)-32)*5/9,1) as celsius_min,
                year,
                mo,
                da,
                state,
                country
                FROM
                `bigquery-public-data.noaa_gsod.gsod199{0}` a
                JOIN
                `bigquery-public-data.noaa_gsod.stations` b
                ON(
                  a.stn=b.usaf
                  AND a.wban=b.wban
                  )
                WHERE (
                      state IS NOT NULL
                      AND max<1000
                      AND min<1000
                      )
                GROUP BY state,
                 year,
                  mo,
                  da,
                  country
                """
        all_data = dict()
        for num_table in range(10):
            query_job = self.client.query(query.format(num_table), location='US')
            query_job.result()
            assert query_job.state == 'DONE'
            all_data['table_199%s' % num_table] = query_job

        return all_data
