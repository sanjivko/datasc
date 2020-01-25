#python code to create the xml file
import xml.etree.ElementTree as ET

# create the file structure
#first creating root element
data = ET.Element('data')
#creating items as child element
items = ET.SubElement(data, 'items')
#item is childs,child element is item.
item1 = ET.SubElement(items, 'item')  
item2 = ET.SubElement(items, 'item')
#defining attributes
item1.set('name','item1')  
item2.set('name','item2')
#defining the values
item1.text = 'item1abc'  
item2.text = 'item2abc'
# create a new XML file with the results
mydata = ET.tostring(data)
myfile = open("xmlfileCreate.xml", "wb")  
myfile.write(mydata)
myfile.close()
