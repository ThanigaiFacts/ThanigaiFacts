import requests
from bs4 import BeautifulSoup
from datetime import datetime
from flask import render_template

class News:
    def __init__(self):
        self.URlNextPage = 0
        self.counter = 0
        self.counterPos = 0
        self.counterInc = 12
        self.soup = ''
        self.content = ''
        self.NewsHeader = []
        self.NewsLink = []
        self.detailNews = []
        self.NewsImg = []
        self.Date = datetime.now().strftime("%d/%m/%y")
        self.URL = "https://www.dailythanthi.com/News/State/"
        self.NewsDomain = "https://www.dailythanthi.com/"

    def clearData(self):
        self.counterPos = 0
        self.URlNextPage = 0
        self.NewsHeader = []
        self.NewsLink = []
        self.NewsImg = []
        self.detailNews = []

    def generateNewsWithImg(self):
        req = requests.get(f"{self.URL}{self.URlNextPage}")
        self.soup = BeautifulSoup(req.content, 'html.parser')
        a_tags = self.soup.findAll("div", class_="ListingNewsWithMEDImage")

        for tag in a_tags:
            a_tag = tag.find('a')
            link = a_tag['href']
            img = a_tag.find('img')
            img_src = img['data-src']
            title = img['alt']

            self.NewsHeader.append(title)
            self.NewsLink.append(f"{self.NewsDomain}{link}")
            self.NewsImg.append(img_src)

        for newslink in self.NewsLink:
            res = requests.get(newslink)
            soup = BeautifulSoup(res.content, 'html.parser')
            self.content = soup.find_all("div", class_="details-content-story")[-1].get_text()
            self.detailNews.append(self.content)

    def generateDetailedNews(self):
        res = requests.get(self.NewsLink[self.counter])
        soup = BeautifulSoup(res.content, 'html.parser')
        self.content = soup.find_all("div", class_="details-content-story")[-1].get_text()

    def loadNews(self, num):
        if num > self.URlNextPage:
            self.URlNextPage += 1
            self.generateNewsWithImg()
            if self.URlNextPage <= 1:
                self.counterPos = 0
            else:
                self.counterPos += self.counterInc

