import datetime
import time

import pandas
import yagmail

from news import NewsFeed


def send_email():
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-$d')
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today,
                         language="en")

    email = yagmail.SMTP(user="", password="")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today."
                        f"\n\n{news_feed.get()}")


while True:
    if datetime.datetime.now().hour == 15 and datetime.datetime.now().minute == 41:
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)
