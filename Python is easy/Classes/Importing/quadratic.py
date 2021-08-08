import cmath as m
def quadra(a, b, c):
    minus_b = 0-b
    b_square = b**2
    four_ac = (4*a*c)
    b_square_4ac = b_square - four_ac
    root_b_square_4ac = m.sqrt(b_square_4ac)
    x = minus_b + root_b_square_4ac/2*a
    x1 = minus_b - root_b_square_4ac/2*a
    #return x
    #return x1
    print(x)
    print(x1)
solution = quadra(5, 6, 1)
print(solution)



    