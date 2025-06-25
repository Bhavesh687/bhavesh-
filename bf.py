

num = int(input("Enter a number: "))
factorial = 1
i = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    while i <= num:
        factorial =factorial* i
        i=i+1
    print(f"The factorial of {num} is {factorial}")
