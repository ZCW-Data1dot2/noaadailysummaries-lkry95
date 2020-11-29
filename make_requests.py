import json
import requests

increment = 1000
url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/"
headers = {"token": "JnskqlFozmUWRgZZLRtNQGDwJKPaneqm"}
params = {"limit": increment, "datasetid": "GHCND", "locationid": "FIPS:10003","startdate": "2018-01-01","enddate":"2018-01-31"}

name = "locations_" + + ".json"
with open(name, 'w') as f:
    json.dump(r_json, f)

