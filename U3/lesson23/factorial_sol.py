#recursive
def factorial_rec(n):
    if n == 0:
        return 1
    return(n * factorial_rec(n-1))

# Iterative
def factorial_it(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return(f)

print(factorial_it(7))
print(factorial_rec(7))
