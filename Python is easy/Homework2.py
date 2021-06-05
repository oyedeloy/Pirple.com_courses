
# This file provides a brief description of my favorite song "Ballerina Girl"

Artist = "Lionel Richie"

""" 
Lionel is an award winning pop singer who sold
over 90 million records worldwide during the course of his career.
"""
Genre = "Soul"
Recorded = "Winter 1985"
Label = "Motown"
# An American record label owned by the Universal Music Group
Producers = "Lionel Richie and James Anthony Carmichael"
"""
Carmichael was famous arranging and producing artists such as 
The Commodores, Atlantic Starr, Diana Ross and Lionel Richie
"""
YearReleased = "1986"
Album = "Dancing in the ceiling"
# The album was originally to be titled Say You, Say Me
DurationINseconds = 338



def NameOfArtist ():
    global Artist
    return Artist

def Artist_genre ():
    global Genre
    return Genre

def Song_year ():
    global YearReleased
    return YearReleased

Name_of_artist = NameOfArtist()
print(Name_of_artist)

Genre_type = Artist_genre()
print("Genre is " + Genre_type)

Release_year = Song_year()
print(Release_year)