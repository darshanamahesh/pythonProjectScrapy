import scrapy
from scrapy.spiders import CrawlSpider, Rule

from bs4 import BeautifulSoup
import urllib


class BayutSpider(scrapy.Spider):
    name = "bayut"
    allowed_domains = ['bayut.com']
    start_urls = [
        'https://www.bayut.com/to-rent/property/dubai/'
    ]



    def parse(self, response):
        nextpageurl = response.xpath("//a[@title='Next']/@href")

        yield from self.scrape(response)

        if nextpageurl:
            path = nextpageurl.extract_first()
            nextpage = response.urljoin(path)
            print(format(nextpage))
            yield scrapy.Request(nextpage, callback=self.parse)

    def scrape(self, response):
        for resource in response.xpath("//div[@class='title']/.."):
            #items = HotelscrapItem()

            details = response.css('._0c571c5f').css('::text').extract()


            yield {
                'next_page_details': details

            }

    # Loop over each item on the page.
    #def parse_categories(self,response):



    #def parse(self, response):

       # div = response.css('div').extract()
        #yield {'divtext::text' : div}

        #for next_page in response.css('._6681ac2b'):
          #  yield response.follow(next_page, self.parse)
