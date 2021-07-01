import getpass
import os
import requests
import time
from Law import Law
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
from datetime import date

# IMPORTANT: RUN FROM THE OUTERMOST DIRECTORY
link = "https://www.congress.gov/search?pageSort=latestAction%3Adesc&q=%7B%22source%22%3A%" \
       "22legislation%22%2C%22bill-status%22%3A%22law%22%7D"

EMAIL_ADDRESS = None
password = None


def main():
    global EMAIL_ADDRESS, password
    print(os.getcwd())
    EMAIL_ADDRESS = input("Email? ")
    password = getpass.getpass(prompt="Password? ")
    # re_init()
    message = make_email_message()
    send_email(message)


def make_email_message():
    f = open("backend/.info/most-recent.txt", "r")
    recent_title = f.read()
    f.close()
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    law_blocks = [Law(law) for law in soup.find_all(class_="expanded", limit=10)]
    message = ""
    for law in law_blocks:
        if law.title == recent_title:
            break
        message += str(law)
    if message:
        return message
    return None


def send_email(message):
    msg = EmailMessage()
    d = date.today().strftime("%B %d, %Y")
    msg['Subject'] = 'New Laws Passed on {today}!'.format(today=d)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] =   # Change later
    msg.set_content(message)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, password)
        smtp.send_message(msg)


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
        recent_title = soup.find(class_="result-title bottom-padding").text.strip()
        f = open(".info/most-recent.txt", "w")
        f.write(recent_title)
        f.close()
    else:
        re_init()
        return


if __name__ == "__main__":
    main()
