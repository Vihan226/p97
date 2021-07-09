print("Guessing game!")
import random
a=random.randint(1,9)
c=0


while c<5: 
    b= int(input("Guess a number between 1 and 9!"))
    
    if b<a:
        print("Your guess was too low: Guess a number higher than", b)

    elif b>a:
        print("Your guess was too high", b)

    else :
        print("Congratulations! You have guessed it right")

    c=c+1

if not c<5: 
    print("You lose! The number was   ",a  )

