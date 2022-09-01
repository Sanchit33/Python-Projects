from email.message import EmailMessage
import ssl
import smtplib

email_sender = ' shindesanchit33@gmail.com'
email_password = "rymh vqtp ybhy hont"
email_receiver = 'famoustrends3@gmail.com'

subject = "hey i am a data analyst"
body = """ just wanted to tell you that i build a python program to send emai,l
1000's of mail just by one click, hope you like it
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em[' subject'] =  subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, em.as_string())
