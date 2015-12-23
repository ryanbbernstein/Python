# coding: utf-8
import xml.etree.ElementTree as ET

class SiteMap():
	def __init__(self):	
		self.tree = ET.parse('sitemap.xml')
		self.root = self.tree.getroot()
		self.list = []

	def get(self):
		for child in self.root:
			url = child[0].text
			self.list.append(url)
		return self.list