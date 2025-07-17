## creating a Guessing game using conditional statement

PredeinedNumber=int(input("Enter the Number that you want to Preduct:"))


print("Enter the Number:>>")
guess=int(input())
if guess<PredeinedNumber:
    print("Please Guess Higher Number")
    guess=int(input("enter the number again"))
    if guess==PredeinedNumber:
        print("you have guessed right Now")
    else:
        print("Sorry, you have not guessed the right Number again")
    
elif guess>PredeinedNumber:
    print("Please Guess lower")
    
else:
    print("great you have guess right")
