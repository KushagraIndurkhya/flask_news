from flask import Flask,render_template
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from datetime import date


app = Flask(__name__)

@app.route('/')
def news_scrape():
    news_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()
    soup_page = soup(xml_page, "lxml")
    news_list = soup_page.findAll("item")
    final_news=[]
    for news in news_list:
            final_news.append(news.title.text)
    today = date.today()
    return render_template("index.html",date=today,news=final_news)


if __name__ == '__main__':
    app.run()
