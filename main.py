import requests
from bs4 import BeautifulSoup


link = input('What website? ')

r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")
expanded = soup.find_all(class_="expanded")
print(str(expanded))


