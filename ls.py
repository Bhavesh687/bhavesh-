def linear_search(num,target):
    for i in range (len(num)):
        if num[i] == target:
            return i
    return -1
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40]
target = 13
result = linear_search(numbers,target)
if result != -1:
    print(f"The number was found at position {result}")
else:
    print(f"The number  was not found")