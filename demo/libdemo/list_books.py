from bs4 import BeautifulSoup

with open("books.xml", "rt") as f:
    contents = f.read()

bs = BeautifulSoup(contents, "lxml-xml")

print("Publisher : ", bs.find("publisher")["name"])

for book in bs.find_all("book"):
    print(f"{book.find('title').text:50} {book.find('author').text}")
