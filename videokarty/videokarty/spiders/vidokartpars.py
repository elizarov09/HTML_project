import scrapy
from scrapy_selenium import SeleniumRequest
import json
import pandas as pd
import os
import logging

class VidokartparsSpider(scrapy.Spider):
    name = "vidokartpars"
    allowed_domains = ["citilink.ru"]
    start_urls = ["https://www.citilink.ru/catalog/videokarty/"]
    custom_settings = {
        'FEEDS': {
            'lighting.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'indent': 4,
            },
        }
    }

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        items = response.css('div.e1ex4k9s0')

        if not items:
            self.log("No items found. Check your CSS selectors.", level=logging.ERROR)

        for item in items:
            name = item.css('a::attr(title)').get()
            link = response.urljoin(item.css('a::attr(href)').get())
            price = item.css('span.Price__main-value::text').get()
            photo = item.css('img::attr(src)').get()

            if not (name and link and price and photo):
                self.log(f"Missing data for item: {item}", level=logging.ERROR)
            else:
                yield {
                    'name': name.strip() if name else 'No name',
                    'link': link,
                    'price': price.strip() if price else 'No price',
                    'photo': photo
                }

        next_page = response.css('a.pagination-next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def closed(self, reason):
        self.log("Starting JSON to Excel conversion...", level=logging.INFO)
        try:
            with open('lighting.json', 'r', encoding='utf-8') as f:
                data = json.load(f)

            if data:
                df = pd.DataFrame(data)
                df.to_excel('lighting.xlsx', index=False)
                self.log("Excel file created: lighting.xlsx", level=logging.INFO)
            else:
                self.log("No data to convert to Excel.", level=logging.ERROR)

            os.remove('lighting.json')
            self.log("Temporary JSON file removed: lighting.json", level=logging.INFO)
        except FileNotFoundError:
            self.log("lighting.json file not found. No data to convert.", level=logging.ERROR)
        except json.JSONDecodeError as e:
            self.log(f"Error decoding JSON: {e}", level=logging.ERROR)
