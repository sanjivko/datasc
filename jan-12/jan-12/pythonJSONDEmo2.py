#python code to convert into dictionary into a json
import json
books={
     "Page":560,
     "Authorname":"Sams",
     "Price":[450,360,375],
     "Publisher":"Wrox",
     "Name":"xml bible"
     }

#json_obj=json.dumps(books)
json_obj=json.dumps(books)
print(json_obj)
json_obj=json.dumps(books,indent=5,sort_keys=True)
print(json_obj)

