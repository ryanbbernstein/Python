# coding: utf-8
import xml.etree.ElementTree as ET

tree = ET.parse('sitemap.xml')
root = tree.getroot()

for child in root:
	url = child[0].text
	print "\"" + url + "\","