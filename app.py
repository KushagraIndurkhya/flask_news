from flask import Flask,render_template
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from datetime import date

today = date.today()
app = Flask(__name__)


@app.route('/')
def hello_world():
    news_url = "https://news.google.com/news/rss"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()
    soup_page = soup(xml_page, "lxml")
    news_list = soup_page.findAll("item")
    final_news=[]
    x = 0
    for news in news_list:
        if (x < 120):
            final_news.append(news.title.text)
            x = x + 1
    print(len(news_list))
    return render_template("index.html",date=today,news= final_news)


if __name__ == '__main__':
    app.run(debug=True)
