a=int(input("Enter a number: "))
if a<=1:
    print(" a is not a prime number ")
else:
     is_prime=True
     for i in range(2,a):
         if a%i==0:
             is_prime=False
             break
if is_prime:
    print(" a is a prime number")
else:
        print(" a is not a prime number")