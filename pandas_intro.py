# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 08:26:59 2020

@author: ojhas
"""

import pandas as pd
import numpy as np
import requests  as req
import json
pd.Series(np.random.normal(1,20,20),index=range(1,21))


response = req.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

data = json.loads(json.dumps(data))

help(response)
s = pd.Series(data, index=range(1, len(data)+1))
index = int(input("Enter index:"))
print (s[index])

pd.Series(5.1, index=range(10))

df = pd.DataFrame(data)

df.head()
df.tail(2)




