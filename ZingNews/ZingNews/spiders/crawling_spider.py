import scrapy
import time

class CrawlingSpider(scrapy.Spider):
    name = "zingnews"
    allowed_domains = ['znews.vn']
    start_urls = ['https://znews.vn/giai-tri.html']

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
            # độ trễ 2 giây
            time.sleep(2)
            yield items