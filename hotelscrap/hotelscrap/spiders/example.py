# -*- coding: utf-8 -*-
import scrapy
from ..items import HotelscrapItem

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ['bayut.com']
    start_urls = ['https://www.bayut.com/property/details-5344432.html']



    def parse(self, response):
        items = HotelscrapItem()

        property_id = response.css('._2663f958+ ._327a3afc').css('::text').extract()
        purpose = response.css('li:nth-child(2) ._812aa185').css('::text').extract()
        type_p = response.css('li:nth-child(1) ._812aa185').css('::text').extract()
        added_on = response.css('li:nth-child(6) ._812aa185').css('::text').extract()
        furnishing = response.css('li:nth-child(4) ._812aa185').css('::text').extract()
        price = response.css('.c4fc20ba').css('::text').extract()
        location = response.css('._1f0f1758').css('::text').extract()
        bed_bath_size = response.css('.fc2d1086 , .fc2d1086 span').css('::text').extract()
        permit_number = response.css('.ff863316~ .ff863316+ .ff863316').css('::text').extract()
        agent_name = response.css('._55e4cba0').css('::text').extract()
        image_url = response.css('._6681ac2b::attr(src)')
        breadcrumbs = response.css('.fontCompensation').css('::text').extract()
        amenities = response.css('.fontCompensation+ ._96aa05ec').css('::text').extract()
        description = response.css('._2a806e1e').css('::text').extract()

        yield {
        'property_id': property_id ,
        'purpose':  purpose,
        'type_p':  type_p,
        'added_on':  added_on,
        'furnishing':  furnishing,
        'price':  price,
        'location':  location,
        'bed_bath_size':  bed_bath_size,
        'permit_number' :  permit_number,
        'agent_name':  agent_name,
        'image_url':  image_url,
        'breadcrumbs':  breadcrumbs,
        'amenities ' :  amenities,
        'description ':  description
        }



