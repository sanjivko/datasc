# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 08:08:36 2020

@author: ojhas




JSON - javascript object notation

"""


import requests
resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()

import json
jdata = json.loads(json.dumps(data))

fobj = open("commets.json", "r")
text = fobj.read()

jdata = json.loads(text)
print (json.dumps(jdata, indent=5, sort_keys=True))

fobj.close()




