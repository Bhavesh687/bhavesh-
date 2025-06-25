a= int(input("enter length of first side"))
b= int(input("enter length of second side"))
c= int(input("enter length of third side"))
if a+b<c and a+c<b and b+c<a and c+b<a:
    print("That is not a triangle")
elif a<=-1 and b<=-1 and c<=-1:
    print("That is not a triangle")
else:
    print("That is  a triangle")
perimeter=a+b+c
print(perimeter)