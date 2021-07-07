import getpass
import requests
import time
from Law import Law
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
from datetime import date, datetime

# IMPORTANT: RUN FROM THE OUTERMOST DIRECTORY
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
        todate = date.today().strftime("%B %d, %Y")
        message = make_email_message()
        send_email(message)
        re_init()


def debug():
    global EMAIL_ADDRESS, password, todate
    EMAIL_ADDRESS = input("Email? ")
    password = getpass.getpass(prompt="Password? ")
    # while True:
        #wait()
    todate = date.today().strftime("%B %d, %Y")
    message = make_email_message()
    send_email(message)
    #re_init()


def wait():
    f = open("backend/.info/next-send.txt", "r")
    target_time = int(f.read().strip())
    f.close()
    while time.time() < target_time:
        time.sleep(10)



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
        message += law.get_contents()["html"]
    if message:
        message += f"[{datetime.now().strftime('%H:%M:%S')}] End of message"
        return message
    return None


def send_email(message):
    msg = EmailMessage()
    msg['Subject'] = 'New Federal Laws Passed on {today}!'.format(today=todate)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'allen.cao.ezio@gmail.com'  # Change later
    msg.add_alternative(message, subtype='html')
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
        f = open("backend/.info/most-recent.txt", "w")
        f.write(recent_title)
        f.close()

        curr_time = time.time()
        next_time = curr_time + (86400 - curr_time % 86400)
        f = open("backend/.info/next-send.txt", "w")
        f.write(str(next_time))
        f.close()
    else:
        re_init()
        return


if __name__ == "__main__":
    run()
