import requests

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print(f'Sorry! Could not get details. Error code : {resp.status_code}')
    exit()

countries = resp.json()
for country in countries:
    print(country['name']['official'])
