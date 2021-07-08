import re
import requests
from bs4 import BeautifulSoup

class Law:
    def __init__(self, law_block):  # law_block is of expanded class
        self.title = law_block.find(class_="result-title").text.strip()
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
        self.html = ""

    def get_contents(self):
        if self.summary and self.html:
            return {"summary:": self.summary, "html": self.html}
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
        paragraphs = summary_element.find_all(["p", "ul"])  # TODO: include "li" elements
        self.summary = ""
        self.html = "<!DOCTYPE html><html><body><h2>{title}</h2>".format(title=self.title)
        for p in paragraphs:
            if p.name == "ul":
                self.html += "<ul>"
                bullet_pts = p.find_all("li")
                for pt in bullet_pts:
                    if pt.text:
                        self.summary += "* {text}".format(text=pt.text)
                        self.summary += "\n\n"
                        self.html += "<li style='color:SlateGray;'>{text}<li>".format(text=pt.text)
                        # TODO: fix appearance of extra non-gray bullet points
                continue
            self.summary += p.text
            self.summary += "\n\n"
            self.html += "<p style='color:SlateGray;'>{text}</p>".format(text=p.text)
        self.html += "</body></html>"
        return {"summary": self.summary, "html": self.html}


    def __repr__(self):
        message = "The '"+ self.title + "' bill was just passed. \n\n" \
                  "It was sponsored by " +  self.sponsor + "\n\n" + \
                  "Here is a quick summary: \n\n" + \
                  self.get_contents()["summary"] + "\n\n"
        return message

    def __str__(self):
        return self.__repr__()


