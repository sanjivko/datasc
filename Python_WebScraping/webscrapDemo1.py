#python code to perform web scrapping using request modules urlopen()
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())
    
