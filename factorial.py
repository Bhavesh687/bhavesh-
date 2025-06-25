n = int(input("Enter a number"))
factorial=1
i=1

if n < 0:
    print("factorial cannot be negative")
else:
    while i <= n:
        factorial =factorial * i
        i=i+1
    print(f"The factorial of {n} is {factorial}")