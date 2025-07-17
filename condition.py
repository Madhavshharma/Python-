#____________if statement___________
# used where we need to define some conditions in our programme like less than and greater than

# for example -> programme of vote given permission 
Name=str(input("please enter your name:"))
age=int(input("please enter your age:"))
if age>=18:
    print(" Mr",Name," you can vote")
    print("sir please enter your voter id ")
else:
    print("sorry sir you cannot vote because your age is below 18")
    print("thank you")
