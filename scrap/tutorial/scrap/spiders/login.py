import scrapy

def authentication_failed(response):
    pass



class LoginSpider(scrapy.Spider):
    name='ex'
    start_urls=['https://www.facebook.com/login.php']

    def parse(self,response):
        return scrapy.FormRequest.from_response(
            response,formdata={'username':'john','password':'secret'},
            callback=self.after_login
        )

    def after_login(self,response):
        if authentication_failed(response):
            self.logger.error('Login Failed')
            return    



        

        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)    