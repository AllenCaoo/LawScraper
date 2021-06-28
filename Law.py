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
        self.action_link = "congress.gov" + action_link
