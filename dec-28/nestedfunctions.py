#python example to understand the nested functions

def f1(msg):   #f1() is outer function
     def f2():      #f2() is inner function
          return "Welcome to "
     return f2()+msg  #calling inner function

#calling the f1() outer function
print(f1("Python Developers"))

   
