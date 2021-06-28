import sys
import re
import requests
from bs4 import BeautifulSoup

class Law:
    def __init__(self, law_block):  # law_block is of expanded class
        self.title = law_block.find(class_="result-title").text
        self.sponsor = law_block.find(class_="result-item").find("a").text
        action_link = None
        for item in law_block.find_all(class_="result-item"):
            for anchor in item.find_all("a"):
                if anchor.text == "All Actions":
                    action_link = anchor.attrs['href']
                    break
        self.action_link = "http://congress.gov" + action_link

    def get_summary(self):
        r = requests.get(self.action_link)
        soup = BeautifulSoup(r.content, "html.parser")
        info_link = soup.findAll("a", text=re.compile('All Information'), href=True)[0]
        return "http://congress.gov" + info_link['href']