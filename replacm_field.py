#-----------replacement fied ------------------
# in this we will cover the topic of .format fucntion

age=24
print("my current age is "+ str(age)+"soon i will be 25")
# we can also print the above statemnt with the help of .format
print("my current age is {0}".format(24)+"soon it will be 25") # here 24 is formatting at {0}

# another example of replacement field
# print("these month have {0} days and they are {1},{2},{3},{4},{5}".format(31,"jan","mar",
#     "may","july","august"))

# 
print(" jan:{0},feb:{1},march:{0},april:{2},may:{0},june:{2},july:{0},august:{0}".format(31,28,30))


#-----------string interpolation-----------------


