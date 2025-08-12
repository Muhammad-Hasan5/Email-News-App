import requests

API_KEY = "2d5c1262afb144338df23ddb5e934b28"
url = ("https://newsapi.org/v2/everything?q=tesl&"
       "from=2025-07-12&sortBy=publishedAt&apiKey="
       "2d5c1262afb144338df23ddb5e934b28")

# make request
request = requests.get(url)
# got data in dictionary form
content = request.json()

# access data
for article in content["articles"]:
    print(article["title"])
    print(article["description"])