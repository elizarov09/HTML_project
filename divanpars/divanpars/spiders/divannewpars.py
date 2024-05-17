import scrapy
import csv


class DivannewparsSpider(scrapy.Spider):
    name = 'divannewpars'
    allowed_domains = ['divan.ru']
    start_urls = ['https://www.divan.ru/category/svet']

    def parse(self, response):
        svets = response.css('div.lsooF')
        with open('svetilniki.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Название', 'Цена', 'Ссылка'])
            writer.writeheader()

            for svet in svets:
                writer.writerow({
                    'Название': svet.css('span::text').get(),
                    'Ссылка': svet.css('link[itemprop="url"]::attr(href)').get(),
                    'Цена': svet.css('span.ui-LD-ZU::text').get()
                })

    '''def parse(self, response):
        svets = response.css('div.lsooF')
        for svet in svets:
            yield{
                'name': svet.css('span::text').get(),
                'link': svet.css('link[itemprop="url"]::attr(href)').get(),
                'price': svet.css('span.ui-LD-ZU::text').get()
            }'''
