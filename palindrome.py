n=int(input())
original = n
reverse = 0

for i in str(n):
    reverse = reverse*10+ int(i)
if reverse == original:
        print("it is a palindrome")
elif reverse != original:
        print("it is not  a palindrome")
