# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelscrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    property_id = scrapy.Field()
    purpose = scrapy.Field()
    type_p = scrapy.Field()
    added_on = scrapy.Field()
    furnishing = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    bed_bath_size = scrapy.Field()
    permit_number = scrapy.Field()
    agent_name = scrapy.Field()
    image_url = scrapy.Field()
    breadcrumbs = scrapy.Field()
    amenities = scrapy.Field()
    description = scrapy.Field()
    pass
