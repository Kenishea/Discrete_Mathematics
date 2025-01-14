# Define the relation R
R = {(1, 'y'), (1, 'z'), (3, 'y'), (4, 'x'), (4, 'z')}

# Define the set A
A = {1, 2, 3, 4}

# Define the set B
B = {'x', 'y', 'z'}

# Check if R is reflexive
reflexive = all((a, a) in R for a in A)
print("Is R reflexive?", reflexive)

# Check if R is symmetric
symmetric = all((b, a) in R for (a, b) in R)
print("Is R symmetric?", symmetric)
