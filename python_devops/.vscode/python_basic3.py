# Import the 'datetime' module to work with date and time
import datetime
import pytz
# Get the current date and time
now = datetime.datetime.now()

# Create a datetime object representing the current date and time

# Display a message indicating what is being printed
print("Current date and time : ")
print(now)
# Print the current date and time in a specific format
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Use the 'strftime' method to format the datetime object as a string with the desired format
future_date= now - datetime.timedelta(days=7)

print(future_date.strftime("%Y:%M:%d %H:%m:%S"))




# Get the current date and time in UTC
now_utc = datetime.datetime.now(pytz.utc)

# Define the target time zones
ist_tz = pytz.timezone('Asia/Kolkata')  # IST
est_tz = pytz.timezone('America/New_York')  # EST

# Convert the current UTC time to the target time zones
now_ist = now_utc.astimezone(ist_tz)
now_est = now_utc.astimezone(est_tz)

# Display a message indicating what is being printed
print("Current date and time in UTC: ")
print(now_utc.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

# Display the current date and time in IST
print("\nCurrent date and time in IST (Indian Standard Time): ")
print(now_ist.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

# Display the current date and time in EST
print("\nCurrent date and time in EST (Eastern Standard Time): ")
print(now_est.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
