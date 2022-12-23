import pandas as pd
import smtplib

SenderAddress = "writingservices989@gmail.com"
password = "ybwhzxddzskjraap"

e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = '''We are Writers
Happy new Year
Good morning
Yes
'''
subject = "Happy new Year"
body = "Subject: {}\n\n{}".format(subject,msg)

for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
