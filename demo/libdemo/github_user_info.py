import requests

resp = requests.get("https://api.github.com/users/srikanthpragada")
if resp.status_code != 200:
    print(f'Sorry! Could not get details. Error code : {resp.status_code}')
    exit()

details = resp.json()
for key, value in details.items():
    print(f"{key:20} {value}")