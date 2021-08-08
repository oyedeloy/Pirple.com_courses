import random

#random.seed(1)
rand_int = random.randint(0, 10)
print(rand_int)
rand_float = random.random() #0.0<=N<1.0 This creates random float between 0 up to but not including 1
print(rand_float)
rand_uniform = random.uniform(1,11) #We have an inclusion of the ending value
print(rand_uniform)