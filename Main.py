import smtplib
import os

print("hello")

api_key = os.getenv("API_KEY")
# Use the api_key in your code

toaddrs = "NyleWagjiani@Gmail.com"
fromaddr = "NyleWagjiani@Gmail.com"
message = "hello"

with smtplib.SMTP("smtp.gmail.com", 587) as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(fromaddr, api_key)

    for i in range(3):
        smtpserver.sendmail(fromaddr, toaddrs, message)
        print(f"Email sent {i+1}")
