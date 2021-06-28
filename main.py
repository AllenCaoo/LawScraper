import requests
from bs4 import BeautifulSoup


link = "https://www.congress.gov/search?pageSort=latestAction%3Adesc&q=%7B%22source%22%3A%" \
       "22legislation%22%2C%22bill-status%22%3A%22law%22%7D"

r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")
law_blocks = soup.find_all(class_="expanded")
for tag in law_blocks:
    title = tag.find(class_="result-title")
    sponsor = tag.find(class_="result-item").find("a")
    print(f"{title.text}, sponsored by {sponsor.text}")


