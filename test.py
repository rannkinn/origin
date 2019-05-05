import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site
        print(self.site)

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()

        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")

            if url is None:
                continue
            elif "https://www." in url:
                print("\n" + url)

news = "https://www.msn.com/ja-jp/"
Scraper(news).scrape()
