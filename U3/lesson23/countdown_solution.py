# Countdown using a for loop
def Countdown_for(n):
    for i in range(n,-1,-1):
        print(i)
# Countdown using recursion
def Countdown_recursion(n):
    if n == 0:
        print(0)
    else:
        print(n)
        Countdown_recursion(n-1)

print("For Loop")
Countdown_for(5)
print("Recursion")
Countdown_recursion(5)
