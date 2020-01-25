#python code to work on other object like list and tuple
import json
print(type(["apple","orange","graped"]))
print("After converting list: ",type(json.dumps(["apple","orange","graped"])))
tobj=tuple(["sachin@gmail.com",145553])
print(type(tobj))
#convert to json type
cvrt=json.dumps(tobj)
print(type(cvrt))  
print("After converting tuple",json.dumps(("sachin@gmail.com",145553)))
