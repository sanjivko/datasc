#python code to design a function to perform input age validations

def validateAge(age):              #formal parameter
     if(age<18 and age>=1):
          return "Minor"
     elif(age>=18 and age<55):
          return "Major"
     else:
          return "Senior Citizen"

#calling the function
print("Yout belong as : ", validateAge(63)) #actual parameter
