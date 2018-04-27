from googleBigQuery.noaa_gsod import NOAA_GSOD

def test_client_conn():
    assert NOAA_GSOD()