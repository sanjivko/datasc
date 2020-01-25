#python code to perform lambda operations

#We can find the difference between normal and lambda

def adds(x,y):
     return x+y

#call the function
print("total: ",adds(120,20))

#defining the lambda
res=lambda a,b:a+b
print("sum is: ",res(120,3))
