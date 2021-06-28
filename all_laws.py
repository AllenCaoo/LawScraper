import requests
from bs4 import BeautifulSoup
from Law import Law


def get_all_laws():
    link = "https://www.congress.gov/search?pageSort=latestAction%3Adesc&q=%7B%22source%22%3A%" \
           "22legislation%22%2C%22bill-status%22%3A%22law%22%7D"

    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    law_blocks = soup.find_all(class_="expanded")
    for tag in law_blocks:
        tag = Law(tag)
        title = tag.title
        sponsor = tag.sponsor
        action_link = tag.action_link
        print(f"{title}, sponsored by {sponsor}")
        print(action_link)

get_all_laws()


