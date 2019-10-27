def one():
    print("# 1. Fill in the parameters to range, so that this loop prints the numbers 20, 22, 24, 26, and 28.")
    for i in range(20, 30, 2):
        print(i)

def two():
    print("# 2. How many times would this loop execute?")
    ct_2 = 0
    j = 10
    while j > 0:
        ct_2 += 1
        print(j)
        j -= 1
    print("Answer #2: ", ct_2)



def three():
    print("# 3. How would you change this code to make it not be an infinite loop?")
    # k = 10
    # while k > 0:
    #     print(k)
    #     k = k + 1 #is there another way to write this?
    print("Answer #3: Change i + 1 to i - 1 (or i - any positive number)")

def four():
    print("# 4. Change this loop from a for to a while loop")
    # for l in range(1, 10):
    #     print(l)

    #Answer
    # i_4 = 1
    # while i_4 > 10:
    #   print(i_4)
    #   i_4 = i_4 + 1

def five():
    print("# 5. How many times would this loop execute?")
    # m = 100
    # while m > 10:
    #     print(m)
    #     m = m / 1
    print("Answer #5: infinite")

def main():
    one()
    two()
    three()
    four()
    five()

main()
