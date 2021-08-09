import random

rand=random.randint(1,9)
print(rand)
chances =0


while chances <5: 
    
    guess=int(input("Guess a number of 1 to 9: "))

    if guess > rand:
        print("Larger than number")
        chances+=1
    elif guess < rand:
        print("Smaller than number")
        chances+=1
    else:
        print("You won")

if not chances < 5:
    print("You lose")
    print("The number is",rand)
