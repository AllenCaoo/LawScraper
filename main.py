import requests
from bs4 import BeautifulSoup


link = "https://www.congress.gov/search?pageSort=latestAction%3Adesc&q=%7B%22source%22%3A%" \
       "22legislation%22%2C%22bill-status%22%3A%22law%22%7D"

r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")
titles = soup.find_all(class_="result-title bottom-padding")
for tag in titles:
    print(tag.text)


