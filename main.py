import os
import requests
import smtplib, ssl
from dotenv import load_dotenv


load_dotenv()


topic = "tesla"


API_KEY = "2d5c1262afb144338df23ddb5e934b28"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-07-13&"
       "sortBy=publishedAt&"
       "apiKey=2d5c1262afb144338df23ddb5e934b28&"
       "language=en")


# make request
request = requests.get(url)
# got data in dictionary form
content = request.json()


body = ""
for article in content['articles']:
    if article['title'] is not None:
        body = ("Subject: Today's news" + "\n" + str(body)
                + "\n" + str(article['title']) + "\n"
                + str(article['description']) + "\n"
                + str(article['url']) + 2*"\n")


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("email_address")
    password = os.getenv("email_password")

    receiver = os.getenv("email_address")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


body = body.encode("utf-8")
send_email(body)
