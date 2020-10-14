from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from news_crawler_scraper.spiders.eltiempo import SpiderElTiempo



process = CrawlerProcess(get_project_settings())
process.crawl(SpiderElTiempo)
process.start()