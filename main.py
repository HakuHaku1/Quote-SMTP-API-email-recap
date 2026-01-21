import requests
import smtplib
import datetime as dt
import random

#request API
response = requests.get("https://dummyjson.com/quotes/random/1")
response.raise_for_status()
API_quote = response.json()

# date finder
try:
    time_now = dt.datetime.now().weekday()

    weeks = ""

    if time_now == 0:
        weeks = "Monday"
    elif time_now == 1:
        weeks = "Tuesday"
    elif time_now == 2:
        weeks = "Wednesday"
    elif time_now == 3:
        weeks = "Thursday"
    elif time_now == 4:
        weeks = "Friday"
    elif time_now == 5:
        weeks = "Saturday"
    elif time_now == 6:
        weeks = "Sunday"
except ValueError:
    print("weekday value error")

# gmail sendmail
my_gmail = "example@gmail.com"
Password = "yourpassword"
sendgmail = "example@gmail.com"

Connection = smtplib.SMTP("smtp.gmail.com", port= 587)
Connection.starttls()
Connection.login(user= my_gmail, password= Password)
Connection.sendmail(
    to_addrs= sendgmail,
    from_addr= my_gmail,
    msg= f"subject: {weeks} motivational quote od the day! \n\n {API_quote[0]["quote"]} -{API_quote[0]["author"]}"
    )
