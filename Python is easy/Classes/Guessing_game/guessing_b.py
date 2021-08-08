from random import random
import time

randval = random()
print(randval)
upper = 1.0
lower = 0.0
# if guess is too low, change lower to guess and same for upper.


#guess = 0.5
start_time = time.process_time()
while True:
    guess = (upper + lower)/2
    if guess == randval:
        break
    elif guess < randval:
        lower = guess
    else:
        upper = guess
    
end_time = time.process_time()
print(guess)
print("it took us:", end_time-start_time, "seconds" )
    