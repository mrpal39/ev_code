import scrapy
from scrapy.spiders import CSVFeedSpider
from scrapy.spiders import SitemapSpider  

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractor import LinkExtractor
from tuto.items import DemoItem
from scrapy.loader import ItemLoader 
from tuto.items import Demo  

class DemoSpider(CrawlSpider):
    name='demo'
    allowed_domais=["www.tutorialspoint.com"]
    start_url=["https://www.tutorialspoint.com/scrapy/index.htm"]

def parse(self, response): 
   l = ItemLoader(item = Product(), response = response)
   l.add_xpath("title", "//div[@class = 'product_title']")
   l.add_xpath("title", "//div[@class = 'product_name']")
   l.add_xpath("desc", "//div[@class = 'desc']")
   l.add_css("size", "div#size]")
   l.add_value("last_updated", "yesterday")
   return l.load_item()
  # loader = ItemLoader(item = Item())
  # loader.add_xpath('social''a[@class = "social"]/@href')
  # loader.add_xpath('email','a[@class = "email"]/@href')

    # rules =(
    #     Rule(LinkExtractor(allow=(),restrict_xpaths=('')))
    # )

class DemoSpider(CSVFeedSpider): 
   name = "demo" 
   allowed_domains = ["www.demoexample.com"] 
   start_urls = ["http://www.demoexample.com/feed.csv"] 
   delimiter = ";" 
   quotechar = "'" 
   headers = ["product_title", "product_link", "product_description"]  
   
   def parse_row(self, response, row): 
      self.logger.info("This is row: %r", row)  
      item = DemoItem() 
      item["product_title"] = row["product_title"] 
      item["product_link"] = row["product_link"] 
      item["product_description"] = row["product_description"] 
      return item

class DemoSpider(SitemapSpider): 
   urls = ["http://www.demoexample.com/sitemap.xml"] 
   
   rules = [ 
      ("/item/", "parse_item"), 
      ("/group/", "parse_group"), 
   ]  
   
   def parse_item(self, response): 
      # you can scrap item here  
   
   def parse_group(self, response): 
      # you can scrap group here 