from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from news_crawler_scraper.spiders.lanacion import SpiderLaNacion



process = CrawlerProcess(get_project_settings())
process.crawl(SpiderLaNacion)
process.start()