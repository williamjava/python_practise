1.基于python的爬虫框架——Scrapy

Python开发的一个快速,高层次的屏幕抓取和web抓取框架，用于抓取web站点并从页面中提取结构化的数据。Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试。

2.安装

sudo pip install Scrapy

scrapy version

3.使用

scrapy startproject book_project

scrapy genspider bookinfo amazon.com

scrapy crawl bookinfo -o books.csv
