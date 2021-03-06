import scrapy
import pandas as pd
from . import utils
# xpath
# links = //div[@class="seccion"]//a[@class="boton page-link"]/@href
# title = //div[@class="content_grid_margin"]//h1[@class="titulo"]/text()
# Subtite = //div[@class="content_grid_margin"]//div[@class="lead"]/p/text()
# publication_date = //div[@class="articulo-autor"]//div[@class="fecha-publicacion-bk"]/span/text()
# body = //div[@class="articulo-contenido"]//div[@class="modulos"]/p/text()
# img url = //div[@class="articulos"]//div[@class="figure-apertura-bk"]//meta[@itemprop="url"]/@content

class SpiderElTiempo(scrapy.Spider):
    name = 'eltiempo'
    start_urls = [
        'https://www.eltiempo.com/cultura/entretenimiento',
        'https://www.eltiempo.com/politica',
        'https://www.eltiempo.com/deportes',
        'https://www.eltiempo.com/tecnosfera',
        'https://www.eltiempo.com/salud',
        'https://www.eltiempo.com/vida',
        'https://www.eltiempo.com/economia',
        'https://www.eltiempo.com/cultura'
    ]
    custom_settings = {
        #'FEED_URI': 'eltiempo.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links = response.xpath('//div[@class="seccion"]//a[@class="boton page-link"]/@href').getall()
        for link in links:
            yield response.follow(link, callback = self.parse_link, cb_kwargs={'url': response.urljoin(link)})


    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//div[@class="content_grid_margin"]//h1[@class="titulo"]/text()').get()
        subtitle = response.xpath('//div[@class="content_grid_margin"]//div[@class="lead"]/p/text()').get()
        article_date = response.xpath('//div[@class="articulo-autor"]//div[@class="fecha-publicacion-bk"]/span/text()').get()
        body_html = response.xpath('//div[@class="articulo-contenido"]//div[@class="modulos"]/p/text()').getall()

        body = utils.format_body(body_html)
        
        image_url = response.xpath('//div[@class="articulos"]//div[@class="figure-apertura-bk"]//meta[@itemprop="url"]/@content').get()

        category_translator = {
            'politica': 1,
            'deportes': 3,
            'tecnosfera': 6,
            'salud': 7,
            'vida': 7,
            'economia': 2,
            'cultura': 4,
            'entretenimiento': 5
        }
        category = 8
        try:
            cat_str = link.split('.com/')[1].split('/')[0]
            cat_str_ent = link.split('.com/')[1].split('/')[1]

            if cat_str_ent=='entretenimiento':
                category = 5
            else:
                category = category_translator[cat_str]
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
            'image_url': image_url,
            'category_id': category,
            'journal_id': 1,
            'scraping_date': str(date)
        }

        

 