from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from news_crawler_scraper.spiders.eluniversal import SpiderElUniversal



process = CrawlerProcess(get_project_settings())
process.crawl(SpiderElUniversal)
process.start()