import scrapy


class NotebookSpider(scrapy.Spider):
    name = "notebook"
    allowed_domains = ["www.mercadolivre.com.br"]
    start_urls = ["https://www.mercadolivre.com.br"]

    def parse(self, response):
        pass
