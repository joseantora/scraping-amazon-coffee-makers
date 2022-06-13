import scrapy

MAX_COFFEE_MAKERS = 10

class CoffeeMakerSpider(scrapy.Spider):
    name = 'coffee_makers'
    start_urls = ['https://www.amazon.com/s?k=coffee+maker']

    def parse(self, response):
        products = response.xpath('//*[@data-asin]')
        products = products[:MAX_COFFEE_MAKERS]

        for product in products:
            asin = product.xpath('@data-asin').extract_first()
            if asin:
                product_url = f"https://www.amazon.com/dp/{asin}"
                print('product_url', product_url)
                yield scrapy.Request(url=product_url, callback=self.parse_coffee_maker_page)

        next_page = response.xpath('//a[contains(@href, "page=")]').attrib['href']
        if next_page:
            next_page_url = f"https://www.amazon.com/{next_page}"
            print('NEXT: ',  next_page_url)
            yield response.follow(next_page_url, callback=self.parse)

    def parse_coffee_maker_page(self, response):
        product_name = response.css('#productTitle::text').get()
        ratings = response.css('.review-rating > span::text').getall()
        reviews = response.css('.a-expander-partial-collapse-content span::text').getall()
        for i in range(len(ratings)):
            coffee_maker = {
                'name': product_name,
                'rating': ratings[i],
                'review': reviews[i]
            }
            print(coffee_maker)
            yield coffee_maker
