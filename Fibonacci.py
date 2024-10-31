# A python code that requests the user to enter a number n and displays fibonacci numbers till this number n

n = int(input("Enter the number n: "))

a1 = 0
a2 = 1

for i in range(n) :
    print(a1)
    a = a1 + a2
    a1 = a2
    a2 = a