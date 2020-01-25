#python code using BeautifulSoup to find tags based class attrib
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

#find all the text with word "the prince"
nameList = bsObj.findAll(text="the prince")
print(len(nameList))


#The keyword argument allows you to select tags that contain a particular attribute.
#For example:
allText = bsObj.findAll(id="text")
print(allText[0].get_text())
