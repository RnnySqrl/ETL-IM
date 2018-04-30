# ETL-IM

#### Introduction
>The purpose of the ETL-IM is to get specific data from `bigquery-public-data:noaa_gsod´ BigQuery dataset.
>The data that we need is the minimum and maximum daily temperatures in degrees Celsius by state between the years 1990 and 2000.
>Whe we get all of it, we load to our MySQL database.
>The last thing to do is to check that we have correctly injected our data, to ensure
>that we have created an script which when you pass an state you get an histogram
>for all the minimum an maximum celsius temperatures between the years 1990-2000

#### Installation
```
$ git clone git clone https://github.com/RnnySqrl/ETL-IM.git
$ cd ETL-IM
$ pip3 install -r requirements.txt
$ python3 conf-credentials.py --json directory_where_json_is -m directory_where_main-ini_is
```
#### Tests
````
$ pytest
````

#### Usage
In the root folder of this project, run this command
```
$ python3 ETL_process.py
$ python3 plot_data.py  -s OR
```