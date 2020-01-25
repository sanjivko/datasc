#python map demo with lambda expression

salaries=[50000,45000,70000]

result=map(lambda x:x*(10/100)+x,salaries)
print("Before increment: ",salaries)
print("After increment: ",[data for data in result])
