import smtplib
import os
from datetime import datetime
import pytz
from datetime import timedelta


# Function to send an email
def send_email(api_key, fromaddr, toaddrs, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as smtpserver:
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(fromaddr, api_key)
        smtpserver.sendmail(fromaddr, toaddrs, message)


# Define variables
api_key = os.getenv("API_KEY")
fromaddr = "NyleWagjiani@Gmail.com"
toaddrs = "NyleWagjiani@Gmail.com"

# Set custom start time (12:45:12 AM London Time)
start_time_str = "30/12/2024 12:53:30"  # Set start time in dd/mm/yyyy hh:mm:ss format
start_time = datetime.strptime(start_time_str, "%d/%m/%Y %H:%M:%S")

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

# Format the start and current times in dd/mm/yyyy hh:mm:ss format
start_time_str = start_time.strftime("%d/%m/%Y %H:%M:%S")  # e.g., 01/01/2025 14:51:40
current_time_str = current_time.strftime(
    "%d/%m/%Y %H:%M:%S"
)  # e.g., 02/01/2025 22:51:55

# Send the email with the number of days elapsed and the full date information
message = (
    f"The stopwatch started on {start_time_str}.\n"
    f"The current time is {current_time_str}.\n\n"
    f"The stopwatch has been running for {days_elapsed} days, {hours_elapsed} hours, {minutes_elapsed} minutes, and {seconds_elapsed} seconds!"
)

send_email(api_key, fromaddr, toaddrs, message)
