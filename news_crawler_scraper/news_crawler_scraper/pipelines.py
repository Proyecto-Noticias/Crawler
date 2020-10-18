# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
import json
from itemadapter import ItemAdapter

class NewsCrawlerScraperPipeline(object):
    def process_item(self, item, spider):

        create_item_api_url = os.environ['API_URL']
        requests.post(create_item_api_url+'articles/', data = json.dumps(ItemAdapter(item).asdict()))
        return item
