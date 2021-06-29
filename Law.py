import re
import requests
from bs4 import BeautifulSoup

class Law:
    def __init__(self, law_block):  # law_block is of expanded class
        self.title = law_block.find(class_="result-title").text.strip()
        if self.title[-1] == '.':
            self.title = self.title[:-1]
        self.sponsor = law_block.find(class_="result-item").find("a").text
        action_link = None
        for item in law_block.find_all(class_="result-item"):
            for anchor in item.find_all("a"):
                if anchor.text == "All Actions":
                    action_link = anchor.attrs['href']
                    break
        self.action_link = "http://congress.gov" + action_link
        self.summary = None
        self.info_link = None

    def get_summary(self):
        if self.summary:
            return self.summary
        if not self.info_link:
            r = requests.get(self.action_link)
            soup = BeautifulSoup(r.content, "html.parser")
            all_info = soup.find_all("a", text=re.compile('All Information'), href=True)[0]
            info_link = "http://congress.gov" + all_info['href'] \
                        + "&subjects=hide&relatedBills=hide&committees=hide" \
                          "&cosponsors=hide&allActions=hide&actionsOverview=hide&titles=hide"
            self.info_link = info_link
        r = requests.get(self.info_link)
        soup = BeautifulSoup(r.content, "html.parser")
        summary_element = soup.find("div", id="latestSummary-content")
        paragraphs = summary_element.find_all("p")  # TODO: include "li" elements
        summary = ""
        for p in paragraphs:
            summary += p.text
            summary += "\n\n"
        self.summary = summary
        return summary


    def __repr__(self):
        BOLD = "\033[1m"
        BOLD_END = "\033[0m"
        message = "The '"+ BOLD + self.title + BOLD_END + "' bill was just passed. \n\n" \
                  "It was sponsored by " + BOLD + self.sponsor + BOLD_END + "\n\n" + \
                  "Here is a quick summary: \n\n" + \
                  self.get_summary() + "\n\n"
        return message

    def __str__(self):
        return self.__repr__()

