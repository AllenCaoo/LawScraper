import requests
import time
from Law import Law
from bs4 import BeautifulSoup


link = "https://www.congress.gov/search?pageSort=latestAction%3Adesc&q=%7B%22source%22%3A%" \
           "22legislation%22%2C%22bill-status%22%3A%22law%22%7D"
def main():
    while True:
        re_init()
        f = open(".info/most-recent.txt", "r")
        recent_title = f.read()
        f.close()
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")
        law_blocks = [Law(law) for law in soup.find_all(class_="expanded", limit=10)]
        message = ""
        for law in law_blocks:
            if law.title == recent_title:
                if not message:
                    break
            else:
                message += law
        if message:
            return # TODO: send email
        time.sleep(3600)


def re_init(ask=False):
    if ask:
        want_init = input("Want to re-initialize? y/n ")
    else:
        want_init = "y"
    if want_init == "n":
        return
    elif want_init == "y":
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")
        recent_title = soup.find(class_="result-title bottom-padding").text
        if recent_title[-1] == '.':
            recent_title = recent_title[:-1]
        f = open(".info/most-recent.txt", "w")
        f.write(recent_title)
        f.close()
    else:
        re_init()
        return

if __name__ == "__main__":
    main()