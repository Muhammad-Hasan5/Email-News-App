import requests
import smtplib, ssl


API_KEY = "2d5c1262afb144338df23ddb5e934b28"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2025-07-12&sortBy=publishedAt&apiKey="
       "2d5c1262afb144338df23ddb5e934b28")

# make request
request = requests.get(url)
# got data in dictionary form
content = request.json()

body = ""
for article in content['articles']:
    if article['title'] is None:
        body = (body + article['title'] + "\n"
                + article['description'] + 2*"\n")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "hasanamir8901@gmail.com"
    password = "xyz"

    receiver = "hasanamir8901@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

body = body.encode("utf-8")
send_email(body)
