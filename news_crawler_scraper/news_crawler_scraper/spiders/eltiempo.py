import scrapy

# xpath
# links = //div[@class="seccion"]//a[@class="boton page-link"]/@href

class SpiderElTiempo(scrapy.Spider):
    name = 'eltiempo'
    start_urls = [
        'https://www.eltiempo.com/politica'
    ]
    custom_settings = {
        'FEED_URI': 'eltiempo.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links = response.xpath('//div[@class="seccion"]//a[@class="boton page-link"]/@href').getall()

        print ('\n')
        for link in links:
            print ('https://www.eltiempo.com' + str(link))
            print ('\n')

        print (links_declassified)

        

 