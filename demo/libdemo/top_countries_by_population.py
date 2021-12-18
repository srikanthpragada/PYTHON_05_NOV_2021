import requests

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print(f'Sorry! Could not get details. Error code : {resp.status_code}')
    exit()

countries = resp.json()
top_10_countries = sorted(countries, key=lambda d: d['population'], reverse=True)[:10]
for country in top_10_countries:
    print(f"{country['name']['common']:50}  {country['population']:10}")
