#python code to implement the BeautifulSoup to read html page
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html.read());
#extract <h1> tag data.
print(bsObj.h1)
