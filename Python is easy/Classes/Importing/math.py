import math as m
val = 3
sqrt_val = m.sqrt(val)
print(sqrt_val**2) #**2 is raised to power of 2

exp_val = m.exp(val)
print(exp_val)

#factorial
fact_val = m.factorial(val)
print(fact_val)
sin_val = m.sin(val)
print(sin_val)


a = 5
b = 6
c = 1
minus_b = 0-b
b_square = b**2
four_ac = (4*a*c)
b_square_4ac = b_square - four_ac
root_b_square_4ac = m.sqrt(b_square_4ac)
x = minus_b + root_b_square_4ac/2*a
x1 = minus_b - root_b_square_4ac/2*a


print(x)
print(x1)
