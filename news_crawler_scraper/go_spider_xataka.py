from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from news_crawler_scraper.spiders.xataka import SpiderXataka



process = CrawlerProcess(get_project_settings())
process.crawl(SpiderXataka)
process.start()