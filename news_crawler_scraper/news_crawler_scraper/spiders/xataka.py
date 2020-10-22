import scrapy
import pandas as pd
from . import utils
# xpath
# links = //div[@class="section-recent-list"]//div[@class="abstract-content"]//a/@href
# title = //div[@class="content-container"]//article[@class="article article-normal"]//h1//span/text()
# Subtite = xataca
# publication_date = //div[@class="article-content-wrapper"]//div[@class="article-time"]//time/text()
# body = //div[@class="article-content-wrapper"]//div[@class="blob js-post-images-container"]//descendant-or-self::*
# img url = //div[@class="article-content-wrapper"]//div[@class="article-normal-header-content"]//img/@src

class SpiderXataka(scrapy.Spider):
    name = 'xataka'
    start_urls = [
        'https://www.xataka.com/categoria/ordenadores',
        'https://www.xataka.com/categoria/moviles',
        'https://www.xataka.com/categoria/componentes',
        'https://www.xataka.com/categoria/nuevo',
        'https://www.xataka.com/categoria/pro',
        'https://www.xataka.com/tag/inteligencia-artificial',
        'https://www.xataka.com/categoria/analisis'
    ]
    custom_settings = {
        #'FEED_URI': 'eltiempo.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links = response.xpath('//div[@class="section-recent-list"]//div[@class="abstract-content"]//h2//a/@href').getall()
        for link in links:
            yield response.follow(link, callback = self.parse_link, cb_kwargs={'url': response.urljoin(link)})


    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//div[@class="content-container"]//article[@class="article article-normal"]//h1//span/text()').get()
        subtitle = 'xataka'
        article_date = response.xpath('//div[@class="article-content-wrapper"]//div[@class="article-time"]//time/text()').get()
        body = utils.format_body(response.xpath('//div[@class="article-content-wrapper"]//div[@class="blob js-post-images-container"]//descendant-or-self::*').getall())
        image_url = response.xpath('//div[@class="article-content-wrapper"]//div[@class="article-normal-header-content"]//img/@src').get()
        date = pd.to_datetime('today')

        yield {
            'id': 0,
            'article_url': link,
            'title': title.rstrip().strip(),
            'subtitle': subtitle.rstrip(),
            'article_date': article_date.strip(),
            'body': body,
            'image_url': image_url,
            'category_id': 6,
            'journal_id': 4,
            'scraping_date': str(date)
        }