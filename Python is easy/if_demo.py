
click = False
like = 0
click = True
if click == True:
    like += 1
    click = False
    # click is beign reset back to false
print(like)

Temp = 14
Thermo = 15
print(Thermo)
if  Temp <  15:
    Thermo += 5
    
print(Thermo)

Time = "Day"
Sleepy = False
Pyjamas = "off"

if Time == "Night" and Sleepy == True:
    Pyjamas = "On"
    
print(Pyjamas)


def max(a, b):
     if a > b:
         print('a is the max')
     else:
         print('b is the max')

max(1,2)
    