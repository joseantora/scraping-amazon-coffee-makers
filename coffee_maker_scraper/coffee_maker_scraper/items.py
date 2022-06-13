# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoffeeMakerScraperItem(scrapy.Item):
    # define the fields for your item here like:
    p_name = scrapy.Field()
    rating = scrapy.Field()
    review = scrapy.Field()
    pass
