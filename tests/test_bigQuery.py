from googleBigQuery.noaa_gsod import NOAA_GSOD

def test_client_conn():
    # Tests to verify the connection with google API is established
    assert NOAA_GSOD()