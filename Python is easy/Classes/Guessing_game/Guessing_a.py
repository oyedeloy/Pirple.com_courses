from random import randint



rand_val = randint(0 ,100)
while(True):    #While True=True 
    guess = int(input("please enter your guess: "))
    if guess == rand_val:
        break
    elif guess < rand_val:
        print("guess is too low")
    else:
        print("guess is too high")
print("guess was right")
    
    
    