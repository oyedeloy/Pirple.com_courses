word = "oyedele"
Letters = []
for w in word:
    print(w)
    if w == "e":
        print("This is funny")
    Letters.append(w)
    
for x in range (5, 11):
    print(x)
    
for x in range (10):
    print(x)

print(Letters)

"""
THE MODULUS OPERATOR % CHECKS FOR REMAINDER 
6%4 checks what the remainder is when 6 is divided by 4
"""
print(10%2)
even_numbers = []
odd_numbers = []
for n in range(51):
    if n%2 == 0:
        even_numbers.append(n)
    elif n%2 == 1: 
        odd_numbers.append(n)  
print(even_numbers)
print(odd_numbers)         
        
"""
YOU CAN SPECIFY RANGES WITH STEPS
PRINT RANGE 0-10 WITH A STEP OF 2
"""
for n in range(0,11,2):
    print(n)
    
