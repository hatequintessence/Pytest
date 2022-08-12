import requests
import pytest
@pytest.mark.mark1
def test_checkCode_checkDate():
    url = "https://api.nasa.gov/planetary/apod"

    x = requests.get(url, params = {"api_key": "OVIW4Npa8q46pSf87oUYzqd34FVcTRZVlsNoZRsA", "date": "2021-06-10"})

    assert x.status_code == 200 
    assert x.json()["date"] == "2021-06-10"
@pytest.mark.skip
def test_checkCode_checkText():
    url = "https://api.nasa.gov/planetary/apod"

    x = requests.get(url, params = {"api_key": "OVIW4Npa8q46pSf87oUYzqd34FVcTRZVlsNoZRsA", "date": "2021-06-00"})

    assert x.status_code == 400 
    assert x.json()["msg"] == "time data '2021-06-00' does not match format '%Y-%m-%d'"

