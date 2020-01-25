#python code to extract the data from xml file
from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('items.xml') 
print(mydoc)

#here we create the object items and target it to the "item" element or node.
items = mydoc.getElementsByTagName('item')
print(items)
for i in items:
     print(i)     
print("Number of child Elements %d " % items.length)
#Code to get the values from the node/element/tag
fobj=open("xmldata.csv","w")
print("Content Each Child Element")
fobj.write("A\t,B\t,C\n")
for elem in items:  
    print(elem.firstChild.data)
    fobj.write(elem.firstChild.data + ",")
fobj.close()
