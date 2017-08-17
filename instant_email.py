import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE
from email.MIMEBase import MIMEBase
from email.parser import Parser
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from getpass import getpass
import email
import os
import mimetypes
import sys
import json

server = smtplib.SMTP()
server.connect("smtp.gmail.com",587)
server.ehlo()
server.starttls()

def init():
    if( os.path.exists('instant_email_data.json') ):
        with open('instant_email_data.json', 'r') as f:
            data = json.load(f)
        print(data)
        server.login(data['email'], data['password'])
        return

    email_id = raw_input("Gmail ID: ") + "@gmail.com"
    password = getpass()

    ## implement encrypted file storing this once entered
    user_data = { "email":email_id, "password":password }
    
    with open('instant_email_data.json', 'w') as f:
        json.dump(user_data, f)
    
def send_email(email_id):
   # fromaddr = raw_input("Your Name: ")
    sub = raw_input("Subject: ")
                                
    print("Body ( type \"<done>\" on a new line when done ): \n") 
    body = ""

    stopword = "<done>"
    while True:
        line = raw_input()
        if line.strip() == stopword:
             break
        body += "%s\n" % line
    fromaddr = 'dhruvvv'
    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = email_id
    msg['Subject'] = sub
    msg.attach(MIMEText(body))
    

    print(fromaddr)
    server.sendmail(fromaddr,email_id,msg.as_string())

init()
send_email(sys.argv[1])

