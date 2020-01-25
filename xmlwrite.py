# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 08:58:58 2020

@author: ojhas
"""

import xml.etree.ElementTree as ET


data = ET.Element('data')
items= ET.SubElement(data, 'items')
item1= ET.SubElement(items, 'item')
item2= ET.SubElement(items, 'item')

item1.set('name', 'item1')
item2.set('name', 'item2')

item1.text = 'item1ac'
item2.text = 'item2ac'


mydata = ET.tostring(data)

file = open("data.xml", "wb")
file.write(mydata)
file.close()



from xml.dom import minidom
xml1 = minidom.parse("data.xml")

data = xml1.getElementsByTagName("data")
data
for i in data:
    items = i.getElementsByTagName('items')
    items
    for j in items:
         item = j.getElementsByTagName('item')
         print ("Dfadsfasdfasdfasd")
         for k in item:
             help(k)
             print(k.firstChild.tag,",",k.firstChild.data)
             




tree = ET.parse("data.xml")
root = tree.getroot()
print(root)

# find the first 'item' object
for elem in root:  
    for subelem in elem.findall('item'):
        print (subelem.attrib)
        print (subelem.get('name'))
        print (subelem.text)