import random 

print("NUMBER GUESSING GAME \n Let's play and unwind the game.")

# randint function to generate the random number between 1 to 9 
number=random.randint(1,9)

#number of chances given to player 
chances=0

print("Guess the number between 1 and 9:")

while True:
    
    # Enter a number between 1 to 9
    guess=int(input())
    
    #Compare the user enter number with the number to be guessed
    if guess==number:
        print(f"Congratulations!! You guess the number {number} in {chances} attempts!")
        break
    elif guess<number:
        print("Guess a number higher than", guess)
    else:
        print("Guess a number lower than",guess)
    
    chances+=1
    

    