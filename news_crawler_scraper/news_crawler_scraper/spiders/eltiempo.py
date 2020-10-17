import scrapy
import pandas as pd
# xpath
# links = //div[@class="seccion"]//a[@class="boton page-link"]/@href
# titlle = //div[@class="content_grid_margin"]//h1[@class="titulo"]/text()
# Subtite = //div[@class="content_grid_margin"]//div[@class="lead"]/p/text()
# publication_date = //div[@class="articulo-autor"]//div[@class="fecha-publicacion-bk"]/span/text()
# body = //div[@class="articulo-contenido"]//div[@class="modulos"]/p/text()
# img url = //div[@class="articulos"]//div[@class="figure-apertura-bk"]//meta[@itemprop="url"]/@content

class SpiderElTiempo(scrapy.Spider):
    name = 'eltiempo'
    start_urls = [
        'https://www.eltiempo.com/politica',
        'https://www.eltiempo.com/deportes',
        'https://www.eltiempo.com/tecnosfera',
        'https://www.eltiempo.com/salud',
        'https://www.eltiempo.com/vida',
        'https://www.eltiempo.com/economia',
        'https://www.eltiempo.com/cultura'
    ]
    custom_settings = {
        'FEED_URI': 'eltiempo.json',
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
        body_paragraphs = response.xpath('//div[@class="articulo-contenido"]//div[@class="modulos"]/p/text()').getall()

        body = ""
        for paragraph in body_paragraphs:
            body = body + paragraph.rstrip() + '\n'
        
        image_url = response.xpath('//div[@class="articulos"]//div[@class="figure-apertura-bk"]//meta[@itemprop="url"]/@content').get()

        category_translator = {
            'politica': 'politics',
            'deportes': 'sports',
            'tecnosfera': 'technology',
            'salud': 'health-lifestyle',
            'vida': 'health-lifestyle',
            'economia': 'economy',
            'cultura': 'culture'
        }
        
        category = category_translator[link.split('.com/')[1].split('/')[0]]
        date = pd.to_datetime('today')


        yield {
            'articule_url': link,
            'title': title.rstrip(),
            'sulbtitle': subtitle.rstrip(),
            'article_date': article_date.strip(),
            'body': body,
            'image_url': image_url,
            'category': category,
            'journal_id': 0,
            'scraping_date': date
        }

        

 