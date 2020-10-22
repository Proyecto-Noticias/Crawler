import scrapy
import pandas as pd

from . import utils

# xpath
# links = //div[@id="wrapper"]//section[@class="listado"]/article/h2/a/@href
# title = //div[@id="wrapper"]//article[@id="nota"]//h1/text()
# Subtite = //div[@id="wrapper"]//section[@id="cuerpo"]//epigrafe/text()
# publication_date = //div[@id="wrapper"]//div[@class="barra"]//section[@class="fecha"]/text()
# body = //div[@id="wrapper"]//section[@id="cuerpo"]//p/descendant-or-self::*
# img url = //div[@id="wrapper"]//section[@id="cuerpo"]/figure//picture/source/@srcset

class SpiderLaNacion(scrapy.Spider):
    name = 'lanacion'
    start_urls = [
        'https://www.lanacion.com.ar/politica/',
        'https://www.lanacion.com.ar/deportes/futbol/',
        'https://www.lanacion.com.ar/deportes/tenis/',
        'https://www.lanacion.com.ar/deportes/rugby/',
        'https://www.lanacion.com.ar/tema/tecnologia-tid47502/',
        'https://www.lanacion.com.ar/salud/',
        'https://www.lanacion.com.ar/economia/comercio-exterior/',
        'https://www.lanacion.com.ar/cultura/'
    ]
    custom_settings = {
        #'FEED_URI': 'lanacion.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }


    def parse(self, response):
        links = response.xpath('//div[@id="wrapper"]//section[@class="cuerpo"]//article//h2//a/@href').getall()
        for link in links:
            yield response.follow(link, callback = self.parse_link, cb_kwargs={'url': response.urljoin(link)})

# xpath
# links = //div[@id="wrapper"]//section[@class="cuerpo"]//article//h2//a/@href
# title = //div[@id="wrapper"]//article[@id="nota"]//h1/text()
# Subtitle = //div[@id="wrapper"]//section[@id="cuerpo"]//epigrafe/text()
# publication_date = //div[@id="wrapper"]//div[@class="barra"]//section[@class="fecha"]/text()
# body = //div[@id="wrapper"]//section[@id="cuerpo"]//p/descendant-or-self::*
# img url = //div[@id="wrapper"]//section[@id="cuerpo"]/figure//picture/source/@srcset

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//div[@id="wrapper"]//article[@id="nota"]//h1/text()').get()
        subtitle = response.xpath('//div[@id="wrapper"]//section[@id="cuerpo"]//epigrafe/text()').get()
        article_date = response.xpath('//div[@id="wrapper"]//div[@class="barra"]//section[@class="fecha"]/text()').get()
        body_html = response.xpath('//div[@id="wrapper"]//section[@id="cuerpo"]//p/descendant-or-self::*').getall()

        body = utils.format_body(body_html)
        
        image_url = response.xpath('//div[@id="wrapper"]//section[@id="cuerpo"]/figure//picture/source/@srcset').get()

        category_translator = {
            'politica': 1,
            'deportes': 3,
            'tecnologia': 6,
            'salud': 7,
            'vida': 7,
            'economia': 2,
            'cultura': 4
        }
        category = 8
        try:
            category = category_translator[link.split('.com.ar/')[1].split('/')[0]]
        except KeyError:
            print('Category not listed')

        date = pd.to_datetime('today')

        yield {
            'id': 0,
            'article_url': link,
            'title': title.rstrip(),
            'subtitle': subtitle.rstrip(),
            'article_date': article_date.strip(),
            'body': body,
            'image_url': 'https:'+image_url,
            'category_id': category,
            'journal_id': 2,
            'scraping_date': str(date)
        }


        




        


    
        

 