from types import resolve_bases
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError,TCPTimedOutError



class DemoSpider(scrapy.Spider):
    name='demo'
    start_urls=[
        "http://www.httpbin.org/",              # HTTP 200 expected 
        "http://www.httpbin.org/status/404",    # Webpage not found  
        "http://www.httpbin.org/status/500",    # Internal server error 
        "http://www.httpbin.org:12345/",        # timeout expected 
        "http://www.httphttpbinbin.org/",      
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u,callback=self.parse_httpbin),
            dont_filter=True


    def parse_httpbin(self, response): 
      self.logger.info('Recieved response from {}'.format(response.url)) 
      # ...  


    def  errback_httpbin(self,failure):
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            response=failure.value.response
            self.logger.error('htttp Error occireed on %s',response.url)

        elif failure.check(DNSLookupError) :
            response=failure.request
            self.logger.error("DNSLookupError occurred on %s", request.url) 

        elif failure.check(TimeoutError,TCPTimedOutError):
            request =failure.request
            self.logger.eerror("timeout occured on %s",request.url)    
 



