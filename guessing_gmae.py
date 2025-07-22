# ## creating a Guessing game using conditional statement

# PredeinedNumber=int(input("Enter the Number that you want to Preduct:"))


# print("Enter the Number:>>")
# guess=int(input())
# if guess<PredeinedNumber:
#     print("Please Guess Higher Number")
#     guess=int(input("enter the number again"))
#     if guess==PredeinedNumber:
#         print("you have guessed right Now")
#     else:
#         print("Sorry, you have not guessed the right Number again")
    
# elif guess>PredeinedNumber:
#     print("Please Guess lower")
    
# else:
#     print("great you have guess right")



## Using the Conditional operator to run the above code 
answer=8
guess=int(input("Please enter the Number:-"))
# if guess != answer:
#     print("you have Not guess right")
#     guess=int(input("enter the value again:-"))
#     if guess<answer:
#         print("Please Guess Higher")
#     elif guess>answer:
#         print("Please Guess Lower")
#     else:
#         print("you have now guess right")
# else:
#     print("You have guess Right on first chance")


## changing the condition from != to ==
if guess==answer:
    print("You have guess the Right on first chance")
else:
    guess=(int(input()))
    if guess<answer:
        print("Please Guess higher")
    elif guess>answer:
        print("Please Guess Lower")
    else:
        print("Now you have guess the Correct")
        
    
    