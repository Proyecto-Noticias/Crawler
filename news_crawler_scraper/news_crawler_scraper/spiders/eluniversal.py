import scrapy
import pandas as pd
from . import utils


class SpiderElUniversal(scrapy.Spider):
    name = 'eluniversal'
    start_urls = [
        'https://www.eluniversal.com.mx/nacion',
        'https://www.eluniversal.com.mx/deportes',
        'https://www.eluniversal.com.mx/techbit',
        'https://www.eluniversal.com.mx/ciencia-y-salud'
    ]
    custom_settings = {
        #'FEED_URI': 'eltiempo.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links = response.xpath('//div[@class="contenido-principal"]//div[@class="panel-panel"]//h2//a/@href').getall()

        print('\n'*3)
        print(links)
        print('\n'*3)
        for link in links:
            yield response.follow(link, callback = self.parse_link, cb_kwargs={'url': link})


    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//div[@class="contenido-principal"]//h1/text()').get()
        subtitle = response.xpath('//div[@class="contenido-principal"]//h2/text()').get()
        article_date = response.xpath('//div[@class="contenido-principal"]//div[@class="ce12-DatosArticulo "]//span[@class="ce12-DatosArticulo_ElementoFecha"]/text()').get()
        body_html = response.xpath('//div[@class="contenido-principal"]//div[@class="gl-Grid_7nota"]//descendant-or-self::*').getall()

        body = utils.format_body(body_html)
        
        image_url = response.xpath('//div[@class="contenido-principal"]//figure[@class="contenedor-ImagenArticulo"]//img/@src').get()

        category_translator = {
            'nacion': 1,
            'universal-deportes': 3,
            'techbit': 6,
            'ciencia-y-salud': 7,
            'vida': 7,
            'economia': 2,
            'cultura': 4
        }
        category = 8
        try:
            category = category_translator[link.split('.com.mx/')[1].split('/')[0]]
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
            'journal_id': 3,
            'scraping_date': str(date)
        }