#python code to access the xml file and extract the attributes of an element

#python code to extract the data from xml file
from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('items.xml') 
print(mydoc)

#here we create the object items and target it to the "item" element or node.
items = mydoc.getElementsByTagName('item')
#print(items)

# one specific item attribute
print('Item #2 attribute:')  
print(items[1].attributes['name'].value)

# all item attributes
print('\nAll attributes:')  
for elem in items:  
    print(elem.attributes['name'].value)

# one specific item's data
print('\nItem #2 data:')  
print(items[1].firstChild.data)  
print(items[1].childNodes[0].data)
