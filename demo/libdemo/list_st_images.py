import requests
from bs4 import BeautifulSoup
WEBSITE = "http://www.srikanthtechnologies.com"

resp = requests.get(WEBSITE)
contents = resp.text
bs = BeautifulSoup(contents, 'html.parser')
images = bs.find_all("img")
print(f"No. of images = {len(images)}")

for img in images:
    print( WEBSITE + "/" + img["src"])