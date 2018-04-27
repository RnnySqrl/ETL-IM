#!/usr/bin/python3
# -*- coding: utf-8 -*-
from googleBigQuery.noaa_gsod import NOAA_GSOD
from load.database import DataBase
from load.utils import generate_query_data


nooa_gsod = NOAA_GSOD()
result = nooa_gsod.get_data()
for num_table in range(10):
    query = generate_query_data(result['table_199%s' % str(num_table)])
    with DataBase() as db:
        db.insert_data(query)