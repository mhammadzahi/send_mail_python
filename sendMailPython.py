import smtplib, ssl
from email.message import EmailMessage
import time
import random


#read contents
with open("contents.txt", "r") as file_cont:
    contents = file_cont.read().splitlines()

# Read subjects
with open("subjects.txt", "r") as file_sub:
    subjects = file_sub.read().splitlines()

# Read email addresses
with open("data.txt", "r") as file_lst:
    receiver_emails = file_lst.read().splitlines()

# Read senders data
with open("senders.txt", "r") as file_s:
    senders = file_s.read().splitlines()

# Read the PDF file as binary data
with open("att.pdf", "rb") as file:
    pdf_data = file.read()


context = ssl.create_default_context()
for receiver_email in receiver_emails:

    selected_subject = random.choice(subjects).strip()
    selected_content = random.choice(contents)

    selected_sender = random.choice(senders)
    email, password = selected_sender.split(':')

    sender_email = email.strip()
    app_password = password.strip()

    msg = EmailMessage()

    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = selected_subject

    msg.set_content(selected_content)
    #file = open('html_content/c1.txt', 'r')
    #html_content = file.read()
    #file.close()
    #msg.set_content(html_content, subtype='html')
    msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename='file2.pdf')

    time.sleep(5) #wait 5 sec then send
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)


print("Done")