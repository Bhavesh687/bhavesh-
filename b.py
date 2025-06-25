even=0
odd=0
for x in range(1,4):
    if x%2==0:
        even=even+1
    elif x%2!=0:
        odd=odd+1
print(even,odd) 
