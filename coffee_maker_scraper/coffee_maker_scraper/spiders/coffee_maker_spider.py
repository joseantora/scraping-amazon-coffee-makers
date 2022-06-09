import scrapy


MAX_COFFEE_MAKERS = 10

class CoffeeMakerSpider(scrapy.Spider):
    name = 'coffee_makers'

    def start_requests(self):
        urls = [
            'https://www.amazon.com/s?k=coffee+maker'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products = response.xpath('//*[@data-asin]')
        products = products[:MAX_COFFEE_MAKERS]

        for product in products:
            asin = product.xpath('@data-asin').extract_first()
            if asin:
                product_url = f"https://www.amazon.com/dp/{asin}"
                yield scrapy.Request(url=product_url, callback=self.parse_coffee_maker_page)

    def parse_coffee_maker_page(self, response):
        pass
