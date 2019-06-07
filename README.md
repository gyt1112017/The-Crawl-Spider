# The-Crawl-Spider
Crawlspider can crawle regular websites, as it provides a convenient mechanism for following links by defining  a set of rules. More information you can see from this link: https://docs.scrapy.org/en/latest/topics/spiders.html#crawlspider

This introduction is referenced from https://github.com/rafikahmed/web-scraping-course.
More detail, tutorial and information you can find his course (Modern Web Scrapping with Python) on Udemy.
This code is divided in two parts, part one you will create your crawl spider from Scratch and in part two you will build a Pipeline to filter duplicated quotes.

## PART 1
Crawl this website: http://quotes.toscrape.com

Your Crawl Spider must:

Follow the top ten tags links on your right hand side (Please see the image below)

From each tag we only want to extract the quote text

And it must also follow the links in the pagination

Project requirements
Initiate a new Scrapy project and call it: seventh_assignment

Create a new spider class called QuotesToScrapeCrawlSpider

Your spider should be named: quotestoscrapecrawl

Your rules tuple should have only and only two Rules:

One for following the links in the top ten tags

one to click on the next button link

Your spider should only have one parse method called parse_item

All the items should be saved in a JSON file

## PART 2
Now you've built your Crawl Spider but there is a high chance that you noticed your JSON file contains duplicated quotes.

Example:

This quote has two tags: [life, love] which means when we follow the life tag link we will find it listed there and if we follow the love tag we will find it too.

So this time your job is to build a pipeline called FilterDuplicate that will Drop the duplicated quotes.

Hints:
In Python we have a data structure called [sets] which has no duplicates so make sure to use it

Your pipeline should only contain two methods:

open_spider(self, spider) in which you have to instantiate an empty set

process_item(self, item, spider) which should drop the duplicated quotes

In Scrapy if we do want to Drop and item we can use the [DropItem] exception

You can use the following code as a start

from scrapy.exceptions import DropItem
 
class FilterDuplicate(object):
    
    def open_spider(self, spider):
        # instantiate your set here 
 
    def process_item(self, item, spider):
        #check if item is already in your set:
            raise DropItem("Item dropped {0}".format(item.get('quote')))
        else:
            #means if the item doesn't exist in your set then add it to it
            return item
            
[sets]='https://docs.python.org/3/tutorial/datastructures.html#sets'            
[DropItem]='https://doc.scrapy.org/en/latest/topics/exceptions.html#dropitem'
