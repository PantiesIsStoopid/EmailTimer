import smtplib
import os
from datetime import datetime
import pytz
from datetime import timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Function to send an email with a subject
def send_email(api_key, fromaddr, toaddrs, subject, message):
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddrs
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as smtpserver:
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(fromaddr, api_key)
        smtpserver.sendmail(fromaddr, toaddrs, msg.as_string())


# Define variables
api_key = os.getenv("API_KEY")
fromaddr = "NyleWagjiani@Gmail.com"
toaddrs = "NyleWagjiani@Gmail.com"

# Set custom start time (12:45:12 AM London Time)
start_time_str = "2025-01-17 20:43:45"  # Change this to your desired start time
start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")

# Define the London timezone
london_tz = pytz.timezone("Europe/London")

# Localize the start time to London timezone (make it timezone-aware)
start_time = london_tz.localize(start_time)

# Get the current time in London timezone (timezone-aware)
current_time = datetime.now(london_tz)

# Calculate the elapsed time as a timedelta object
elapsed_time = current_time - start_time

# Calculate full days and partial hours/minutes
days_elapsed = elapsed_time.days
# Convert remaining seconds to hours and minutes
remaining_seconds = elapsed_time.seconds
hours_elapsed = remaining_seconds // 3600
minutes_elapsed = (remaining_seconds % 3600) // 60
seconds_elapsed = remaining_seconds % 60

# Format the start and current times in a readable way
start_time_str = start_time.strftime(
    "%d %B %Y, %I:%M:%S %p"
)  # e.g., 02 January 2025, 12:45:12 AM
current_time_str = current_time.strftime(
    "%d %B %Y, %I:%M:%S %p"
)  # e.g., 02 January 2025, 12:45:12 AM

# Email subject
subject = (f"Stopwatch {days_elapsed}")

# Email message
message = (
    f"The stopwatch has been running for {days_elapsed} days, {hours_elapsed} hours, {minutes_elapsed} minutes, and {seconds_elapsed} seconds!"
)

# Send the email with the subject and message
send_email(api_key, fromaddr, toaddrs, subject, message)
