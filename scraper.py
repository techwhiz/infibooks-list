# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
import scraperwiki           
import lxml.html
import re
import urlparse         

url = "http://www.infibeam.com/best-selling-books"
html = scraperwiki.scrape(url)
authors =''
tree = lxml.html.fromstring(html)

#bk_titles=tree.xpath('//*[contains(@class,"carousel_list")]//*[contains(@class,"productlist_index")]//*[contains(@class,"product-img")]//img/@title')
#bk_isbns=tree.xpath('//*[contains(@class,"carousel_list")]//*[contains(@class,"productlist_index")]//*[contains(@class,"product-img")]//img/@data-title')
bk_urls=tree.xpath('//*[contains(@class,"carousel_list")]//*[contains(@class,"productlist_index")]//*[contains(@class,"product-img")]//a/@href')
#print bk_isbns

for bk_url in bk_urls:
  scraperwiki.sqlite.save(['url'],data={'url':bk_url})
