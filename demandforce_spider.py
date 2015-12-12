import scrapy
from scraper.items import ScraperItem

class DemandForceSpider(scrapy.Spider):
	name = "df"
	allowed_domains = ["local.intuit.com"]
	start_urls = [
		"https://local.intuit.com/d/",
	]
	
	def parse(self, response):
		for state in response.xpath("id('page')/table[1]/tbody"):
			for href in state.css("a::attr('href')"):
				url = response.urljoin(href.extract())
				yield scrapy.Request(url, callback=self.parse_cities)
	
	def parse_cities(self, response):
		for row in response.xpath("id('page')/p"):
			for href in row.css("a::attr('href')"):
				url = response.urljoin(href.extract()+"/dental")
				yield scrapy.Request(url, callback=self.parse_page)
				yield scrapy.Request(url, callback=self.parse_pages)
	
	def parse_pages(self, response):
		for href in response.css("a::attr('href')"):
			if "=" in href.extract():
				if not "1" in href.extract():
					url = response.urljoin(href.extract())
					yield scrapy.Request(url, callback=self.parse_page)
			
	def parse_page(self,response):
		for sel in response.xpath("id('page')/div"):
			item = TutorialItem()
			item['name'] = sel.xpath('h2/a/span/text()').extract()
			item['email'] = sel.xpath('dl[2]/dd[2]/text()').extract()
			item['city'] = sel.xpath('dl[1]/dd/dd/span[1]/text()').extract()
			item['state'] = sel.xpath('dl[1]/dd/dd/span[2]/text()').extract()
			yield item