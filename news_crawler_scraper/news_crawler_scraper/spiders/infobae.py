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

class SpiderInfobae(scrapy.Spider):
    name = 'infobae'
    start_urls = [
        'https://www.infobae.com/america/entretenimiento/',
        'https://www.infobae.com/america/tecno/',
        'https://www.infobae.com/america/cultura/'

    ]
    custom_settings = {
        #'FEED_URI': 'eltiempo.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links = response.xpath('//div[@class="feed-list-container"]//div[@class="card-container height_100"]//a/@href').getall()

        for link in links:
            yield response.follow(link, callback = self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//h1/text()').get()
        subtitle = response.xpath('//h2/text()').get()
        article_date = response.xpath('//div[@class="datetime | display_inline byline_datetime"]/text()').get()
        body_html = response.xpath('//article//p/descendant-or-self::*').getall()

        body = utils.format_body(body_html)
        
        image_url = response.xpath('//picture[@class="font_tertiary visual__image"]//img/@src').get()

        category_translator = {
            'entretenimiento': 5,
            'tecno': 6,
            'cultura': 4
        }
        category = 0
        try:
            category = category_translator[link.split('.com/america/')[1].split('/')[0]]
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
            'journal_id': 5,
            'scraping_date': str(date)
        }



    