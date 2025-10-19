import random 

print("NUMBER GUESSING GAME \n Let's play and unwind the game.")

number=random.randint(1,9)

chances=0

print("Guess the number between 1 and 9:")

while True:
    guess=int(input())
    
    if guess==number:
        print(f"Congratulations!! You guess the number {number} in {chances} attempts!")
        break
    elif guess<number:
        print("Guess a number higher than", guess)
    else:
        print("Guess a number lower than",guess)
    
    chances+=1
    

    