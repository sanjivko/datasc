#python code to implement elementTree
import xml.etree.ElementTree as ET  
tree = ET.parse('items.xml')  
root = tree.getroot()

# total amount of items
print(len(root[0]))


print('Item #2 attribute:')  
print(root[0][1].attrib)

# all item attributes
print('\nAll attributes:')  
for elem in root:  
    for subelem in elem:
        print(subelem.attrib)
