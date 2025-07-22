#In this we will learn about the Nested foor loop in Python 
for i in range(1,13):
    for j in range(1,13):
        print(j,i,i*j)
    print("----"*5)
    
for i in range(1,13):
    for j in range(1,13):
        print("{0} times {1} is {2}".format(j,i,i*j))
    print("-------"*3)
    