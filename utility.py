import requests
import random
import smtplib
import os
from email.message import EmailMessage

def getBlogData():
    # https://mocki.io/fake-json-api --> json website
    #end_point = "https://mocki.io/v1/f4aff8ed-6d04-43e1-ac4f-ce373a4a64e0"
    return requests.get(os.getenv("BLOG_END_POINT")).json()

def randomNumberGenerator():
    return random.randint(1, 10)

def send_mail(name,mail,mobile,msg):
    userName = 'thanigaisolutions@gmail.com'
    passWord = 'xblntktjuvzkkthf'
    senderMail = 'thanigaisolutions@gmail.com'
    receipient_mail = 'thanigaifacts@gmail.com'

    mailMsg = EmailMessage()

    mailMsg['Subject'] = 'Thanigai Facts - New Contact Form!'
    mailMsg['From'] = senderMail
    mailMsg['To'] = receipient_mail
    msgfile = f"Name : {name}\nMail : {mail}\nMobile : {mobile}\nMessage : {msg}"
    mailMsg.set_content(msgfile)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(userName, passWord)
        smtp.send_message(mailMsg)







