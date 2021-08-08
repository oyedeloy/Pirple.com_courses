#from random import randint
#from random import random
#from random import uniform
import random as r
rand_int = r.randint(0, 10)
print(rand_int)
rand_float = r.random() #0.0<=N<1.0 This creates random float between 0 up to but not including 1
print(rand_float)
rand_uniform = r.uniform(1,11) #We have an inclusion of the ending value
print(rand_uniform)

Simple_list = [1, 3, 5, 7, 11]
pick_element = r.choice(Simple_list)
print(pick_element)
r.shuffle(Simple_list)
print(Simple_list)

