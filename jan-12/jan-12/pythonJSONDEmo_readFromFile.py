#python code to convert the json to python
import json

#open file in read mode 
fobj=open("myinfo.json","r") # Open the jsonfile 
jsondata=fobj.read()     #extracting the jsonfile contents
pydata = json.loads(jsondata) #parse and conver it into python dictionary

#the the pydata is python dictionary
print(pydata)
#access the individual data
print(pydata["age"])
print(pydata["state"])
print(pydata['city'])

#extracting the keys and values from json file.
print("Full Details\n")
for k,v in pydata.items():
     print(k, ":" , v)

