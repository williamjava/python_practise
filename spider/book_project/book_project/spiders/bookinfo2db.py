# -*- coding: utf-8 -*-
import scrapy
import mysql.connector
from book_project.items import BookItem

class Bookinfo2dbSpider(scrapy.Spider):
    name = "bookinfo2db"
    allowed_domains = ["allitebooks.com","amazon.com"]
    start_urls = ['http://www.allitebooks.com/security/']

    def execSQL(self, sql, data):
        conn = mysql.connector.connect(user='root', password='root', database='testpy')
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()

    def parse(self, response):
        num_pages = int(response.xpath('//a[contains(@title, "Last Page →")]/text()').extract_first())
        base_url = "http://www.allitebooks.com/security/page/{0}/"
        for page in range(1, num_pages):
            yield scrapy.Request(base_url.format(page), dont_filter=True, callback=self.parse_page)
        pass

    def parse_page(self, response):
        for sel in response.xpath('//div/article'):
            book_detail_url = sel.xpath('div/header/h2/a/@href').extract_first()
            yield scrapy.Request(book_detail_url, callback=self.parse_book_info)


    def parse_book_info(self, response):
        title = response.css('.single-title').xpath('text()').extract_first()
        isbn = response.xpath('//dd[2]/text()').extract_first()
        item = BookItem()
        item['title'] = title
        item['isbn'] = isbn
        amazon_search_url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + isbn
        yield scrapy.Request(amazon_search_url, callback=self.parse_price, meta={ 'item': item })

    def parse_price(self, response):
        item = response.meta['item']
        item['price'] = response.xpath('//span/text()').re(r'\$[0-9]+\.[0-9]{2}?')[0]
        title = item['title']
        isbn = item['isbn']
        price = item['price']
        sql = "insert into book(title,isbn,price) values (%s, %s, %s)"
        data=(title,isbn,price)
        #sql = "insert into book (title,isbn,price) values('test','fsfs1231',12.12)"
        self.execSQL(self, sql, data) 
        yield item


