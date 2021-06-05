for Number in range(1, 101):
    #if Number > 1:
    for x in range(2, Number):
        if Number%x == 0:
            break
    else:
        print(str(Number) + " is Prime")
        
for i in range(2):
    print(i)
    
f = 1
A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
for i in range(0, 3):
     f =f*i
     for j in range(0, 3):
         A[i][j] = f
print(A)



Aritist_key = input("Enter your key:\n")
Artist_value = input("Enter a value for the key\n")
def guess_value(Aritist_key, Artist_value):
    for key, value in Favourite_song.items():        
        if key in Favourite_song.items() and value in Favourite_song.items(): 
            print(True)
        else:
            print(False)
        break
        
    
    
guess_value(Aritist_key, Artist_value)

def guess_value(Aritist_key, Artist_value):
    for key, value in Favourite_song:        
        if Aritist_key in Favourite_song.items() and Artist_value in Favourite_song.items(): 
            print(True)
        else:
            print(False)
        
        
    
    
guess_value(Aritist_key, Artist_value)