# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 08:27:34 2020

@author: ojhas
"""

import tweepy
from textblob import TextBlob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
auth = tweepy.OAuthHandler("UBlJ02XGUgUVriWMNK4bQSAOV", "2ohiaHURKk1ftZflQG3MVIsaznYBZ1UDxUzFc78xs9cYEHKU21")
auth.set_access_token("68362028-gDMdHfwzOftRaCGmS6MAuJQfFwpDDSA31YBXBoUbr", "L7XkD0fpnZDmZHTPZGo2DVMIxs6Y3ZewgEDPZD8OsiONP")

api = tweepy.API(auth)


data = api.search("Narendra Modi", count=100)
len(data)
out = []
for i in data:
    print (i.text)
    blob = TextBlob(i.text)
    if blob.sentiment.polarity > 0:
        out.append("positive")
    elif  blob.sentiment.polarity ==  0:
        out.append("neutral")   
    elif  blob.sentiment.polarity <  0:
        out.append("negative")   
    

df = pd.DataFrame(out)

print(df)
df.columns = ['sentiment']

df.columns

sns.countplot(x="sentiment", data = df)
plt.title("Sentiment on Narendra Modi ")
plt.show()



