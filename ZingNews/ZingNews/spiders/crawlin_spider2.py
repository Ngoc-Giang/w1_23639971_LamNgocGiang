import scrapy
import time

class CrawlingSpider(scrapy.Spider):
    name = "Zingnews"
    allowed_domains = ['znews.vn']
    start_urls = ['https://lifestyle.znews.vn/doi-song.html']

    def parse(self, response):
        news = response.css(".article-item")
        for zingnew in news:
            items = {
                "Title": zingnew.css(".article-title a::text").get(),
                "Date": zingnew.css("span.date::text").get(),
                "Time": zingnew.css("span.time::text").get(),
                "Content": zingnew.css("p.article-summary::text").get(),
                "Link": zingnew.css(".article-title a::attr(href)").get()
            }
            time.sleep(2)
            yield items