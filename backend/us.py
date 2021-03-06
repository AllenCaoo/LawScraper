import getpass
import json
import requests
import time
from Law import USLaw
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
from datetime import date, datetime

# IMPORTANT: RUN FROM THE OUTERMOST DIRECTORY
# To install packages: pip install -r requirements.txt
link = "https://www.congress.gov/search?pageSort=latestAction%3Adesc&q=%7B%22source%22%3A%" \
       "22legislation%22%2C%22bill-status%22%3A%22law%22%7D"

EMAIL_ADDRESS = None
password = None
todate = None


def run():
    global EMAIL_ADDRESS, password, todate
    EMAIL_ADDRESS = input("Email? ")
    password = getpass.getpass(prompt="Password? ")
    while True:
        wait()
        message = make_email_message()
        todate = date.today().strftime("%B %d, %Y")
        send_email(message)
        print_log(len(message) > 0, todate)
        re_init()


def debug():
    global EMAIL_ADDRESS, password, todate
    EMAIL_ADDRESS = input("Email? ")
    password = getpass.getpass(prompt="Password? ")
    todate = date.today().strftime("%B %d, %Y")
    message = make_email_message()
    if message:
        send_email(message)


def wait():
    f = open("backend/.info/next-send.txt", "r")
    target_time = int(f.read().strip())
    f.close()
    while time.time() < target_time:
        time.sleep(10)


def get_subs():
    subs_path = 'public/src/subs.JSON'  # Running script from LawScraper/
    with open(subs_path) as json_file:
        data = json.load(json_file)
        entries = [(name, email) for name, email in data.items()]
    return entries


def make_email_message():
    f = open("backend/.info/most-recent.txt", "r")
    recent_title = f.read()
    f.close()
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    law_blocks = [USLaw(law) for law in soup.find_all(class_="expanded", limit=10)]
    message = ""
    for law in law_blocks:
        if law.title == recent_title:
            break
        message += law.get_contents()["html"]
    if message:
        message += "[{time}] End of message" \
            .format(time=datetime.now().strftime('%H:%M:%S'))
        return message
    return None


def send_email(message):
    if message:
        msg = EmailMessage()
        msg['Subject'] = 'New Federal Laws Passed - {today}!'.format(today=todate)
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = [entry[1] for entry in get_subs()]  # Change later
        msg.add_alternative(message, subtype='html')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, password)
            smtp.send_message(msg)


def print_log(sent, date):
    if sent:
        print("{date}: nothing send".format(date=date))
    else:
        print("{date}: send information on new laws".format(date=date))



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
        f = open("backend/.info/most-recent.txt", "w")
        f.write(recent_title)
        f.close()

        curr_time = time.time()
        next_time = curr_time + (86400 - curr_time % 86400)
        f = open("backend/.info/next-send.txt", "w")
        f.write(str(int(next_time)))
        f.close()
    else:
        re_init()
        return


if __name__ == "__main__":
    run()
