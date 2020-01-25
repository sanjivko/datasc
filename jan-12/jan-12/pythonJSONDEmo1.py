#python code to convert the json to python
import json

#cr
mydata1='{  "name":"Sachin","age":43,"city":"mumbai","email":"sachin@gmail.com"}'

#then parse the json data object mydata1

pydata = json.loads(mydata1)

#the the pydata is python dictionary
print(pydata)

#access the individual data
print(pydata["age"])

