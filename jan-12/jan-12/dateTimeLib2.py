from datetime import *
#from datetime import date
#from datetime import time
#from datetime import datetime
def showDateTime():
    ##DATETIME OBJECTS
    #Get today's date from datetime class
    today=datetime.now()
    print (today)
    # Get the current time
    t = datetime.time(today)
    print("The current time is", t)
    #weekday returns 0 (monday) through 6 (sunday)
    wd=date.weekday(today)
    #Days start at 0 for monday
    days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    
    print("Today is day number %s" % str(wd+1))
    print("which is a " + days[wd])
    print("Current Year: ",today.year)
    print("Current Month: ",today.month)
def show():
     print("hi")

#if __name__== "__main__":
showDateTime()
show()

