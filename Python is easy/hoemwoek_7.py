from pprint import pprint

Favourite_song = {
    "Artist": "Lionel Richie",
     "Genre": "Soul",
     "Recorded": "Winter 1985",
     
     "Producers": "Lionel Richie and James Anthony Carmichael",

     "YearReleased": "1986",
     "Album": "Dancing in the ceiling",

     "DurationINseconds": 338     
}

#PRINT KEYS ONLY

print("\n----- PRINTING KEYS ONLY -----\n")
for key in Favourite_song.keys():
    print(key)

#PRINT VALUES ONLY

print("\n-----PRINTING VALUES ONLY -----\n")
for value in Favourite_song.values():
    print(value)
    
#PRINT ENTIRE DICTIONARY USING REGULAR PRINT

#print("\n____ REGULAR PRINT _____")
#print("Favourite Song", Favourite_song) 
#print(Favourite_song.items())



#PRINT ENTIRE DICTIONARY USING PRETTY PRINT

print("\n-----PRETTY PRINT-----\n")
pprint(Favourite_song)

# FORMATTED PRINT
print('\n-----FORMATTED USING F-STRINGS AND FOR LOOPS-----\n')
for key, value in Favourite_song.items():
    #give me 16 characters of space and right justify it
    #The right justification make the columns allign
    print(f"{key:>20s} :{value}")


Aritist_key = input("Enter your key:\n")
Artist_value = input("Enter a value for the key\n")



def guess_value(Artist_key, Artist_value):
    if key in Favourite_song and Favourite_song.get(Artist_key) == Artist_value:
        #return True
        print("\nYour guess was correct")
    else:
        #return False
        print("\nYour inputs are not valid")

print('\n-----PRINTING RESULTS-----')        
        
guess_value(Aritist_key, Artist_value)