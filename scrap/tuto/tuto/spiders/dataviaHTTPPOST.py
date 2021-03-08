import scrapy  
class DemoSpider(scrapy.Spider): 
   name = 'demo' 
   start_urls = ['http://www.something.com/users/login.php']  
   def parse(self, response): 
      return scrapy.FormRequest.from_response( 
         response, 
         formdata = {'username': 'admin', 'password': 'confidential'}, 
         callback = self.after_login 
      )  
   
   def after_login(self, response): 
      if "authentication failed" in response.body: 
         self.logger.error("Login failed") 
         return  
      # You can continue scraping here