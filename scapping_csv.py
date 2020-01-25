# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 09:56:25 2020

@author: ojhas
"""

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
html = urlopen("https://www.top500.org/list/2018/06/?page=1")

soup  = bs(html.read())

table = soup.find("table")


'''
Heading
'''

    
    csvfile = open("data.csv",newline="\n", mode="w+")
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    
    
    tr = table.find_all("tr")
    
    r_list = []
    for i in tr[0].find_all("th"):        
        r_list.append(i.get_text())
    "|".join(r_list)
    csvwriter.writerow(r_list)    
    
        
    r_list.clear()
    for i in range(1, len(tr)):
        r_data = tr[i].find_all("td")
        for d in r_data:
            print (d.get_text())
            r_list.append(d.get_text())
        "|".join(r_list)
        csvwriter.writerow(r_list)
            
    csvfile.close();
