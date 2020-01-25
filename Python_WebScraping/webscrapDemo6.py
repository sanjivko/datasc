#The solution is to look for something identifying about the tag itself. In this case, we
#can look at the file path of the product images:
from urllib.request import *
#import urlopenfrom
from bs4 import *
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])
