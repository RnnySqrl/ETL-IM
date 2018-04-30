from googleBigQuery.noaa_gsod import NOAA_GSOD
import pytest
from settings.settings import GOOGLE_API_CRED


@pytest.mark.skipif(not GOOGLE_API_CRED, reason="Credentials not iniciated")
def test_client_conn():
    # Tests to verify the connection with google API is established
    assert NOAA_GSOD()
