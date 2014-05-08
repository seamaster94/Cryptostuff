__author__ = 'seamaster'

import requests
from bs4 import BeautifulSoup
import smtplib
import re

r = requests.get("http://www.wieistmeineip.de/")

print(r)

text = r.content

#print(text)

soup = BeautifulSoup(text)
ipdiv = soup.find_all(id="ipv4")
print(str(ipdiv[0]))

session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.ehlo()

session.login('sascha.tribelhorn@gmail.com', 'rakete123')

sender = "sascha.tribelhorn@gmail.com"
recipient = "sascha.tribelhorn@gmail.com"
subject = "My IP"

header = ["From: " + sender,
          "Subject: " + subject,
          "To: " + recipient]

header = "\r\n".join(header)

session.sendmail(sender, recipient, header + "\r\n\r\n" + "hello there \nThis is my IP: " + str(ipdiv[0]))
print("sending done")

session.quit()