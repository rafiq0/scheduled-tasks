import pandas
import os
from random import *
import smtplib
from datetime import datetime

today = datetime.today()
date = (today.day,today.month)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.day,row.month):row for (index,row) in data.iterrows()}
if date in birthday_dict:
    name = birthday_dict[date]["name"]
    email = birthday_dict[date]["email"]
    number = randint(1,3)
    file_path = f"letter_templates/letter_{number}.txt"
    with open(file_path) as file:
        content = file.read()
        new_content = content.replace("[NAME]",name)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        to_email = email
        MY_EMAIL = os.environ.get("MY_EMAIL")
        MY_PASSWORD = os.environ.get("MY_PASSWORD")
        message = f"to:{to_email}\nSubject: HAPPY BIRTHDAY\n\n{new_content}"
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            my_email,
            to_email,
            message
        )
else:
    print("Today is noone's birthday")
