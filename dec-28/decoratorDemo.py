#python decorator Demo

def f1(data):
     data.idno=1
     data.name="sachin"
     data.score=90.34
     return data

@f1    #here we say this line is decorator attachement
def adds(x,y):
     return x+y

#call the function
print("sum is: ",adds(120,2))
print(adds.idno)
print(adds.name)
print(adds.score)
