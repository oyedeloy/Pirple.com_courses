"""
This program prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".
Enjo!!!!!
"""

for Number in range(1, 101):
    if Number == 1:
        print(str(1) + " is not a prime number")
    if Number > 1: # All prime numbers are greater than 1
        for x in range(2, Number):
            if Number%x == 0: #if the Number is divisible by the range in x, that means it's not prime.
                break #Then we don't have to continue with the loop.
        else:
            print(str(Number) + " is Prime")
            continue
        if Number%3 == 0 and Number%5 == 0:
           print("FizzBuzzz")
        elif Number%3 == 0:
           print("fizz")
        elif Number%5 == 0:
           print("Buzz")
        else:
            print(Number)
            
                
    
    
    
    
    