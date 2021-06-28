import sys

import requests
import threading
from bs4 import BeautifulSoup


link = "https://www.congress.gov/search?pageSort=latestAction%3Adesc&q=%7B%22source%22%3A%" \
           "22legislation%22%2C%22bill-status%22%3A%22law%22%7D"
def main():
    init()

def init():
    have_init = input("Want to re-initialize? y/n ")
    if have_init == "n":
        return
    elif have_init == "y":
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")
        recent = soup.find(class_="result-title bottom-padding").text
        f = open(".info/most-recent.txt", "w")
        f.write(recent)
        f.close()
    else:
        init()
        return

if __name__ == "__main__":
    main()