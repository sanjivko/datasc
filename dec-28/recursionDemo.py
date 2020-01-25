#python recursions

def fact(n1):
     if (n1==1):
          return 1
     else:
          return fact(n1-1)*n1  #calling function within the function

#call the function
print("factorial is: ",fact(5))
