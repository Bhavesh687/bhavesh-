SM=int(input("Enter science marks"))
m=int(input("Enter mathematical marks"))
s=int(input("Enter social marks"))
E=int(input("Enter english marks"))
T=int(input("Enter telugu marks "))
c=int(input("Enter computer marks"))
a=SM+m+s+E+T+c
b=600
grade=a*100/b
if(a>600):
    print(" Enter valid marks")
elif  grade>90:
    print("Your grade is A")
elif grade>79:
    print("Your grade is B")
elif grade>69:
    print("Your grade is C")
elif grade>59:
    print("Your grade is D")
else:
    print("Your grade is F")
