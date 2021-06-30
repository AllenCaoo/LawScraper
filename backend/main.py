import getpass

import requests
import time
from Law import Law
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage


link = "https://www.congress.gov/search?pageSort=latestAction%3Adesc&q=%7B%22source%22%3A%" \
           "22legislation%22%2C%22bill-status%22%3A%22law%22%7D"

email_address = None
password = None

def main():
    global email_address, password
    email_address = input("Email? ")
    password = getpass.getpass()
    while True:
        re_init()
        message = make_email_message()
        send_email(message)
        time.sleep(3600)


def make_email_message():
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
        return message
    return None


def send_email(message):
    msg = EmailMessage()
    msg['Subject'] = 'New Laws Passed!'
    msg['From'] = email_address
    msg['To'] = 'YourAddress@gmail.com'  # Change later
    msg.set_content(message)


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