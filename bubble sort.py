def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return  arr

my_list = [12,10,13,14,15,16,17,8]
sorted_list = bubble_sort(my_list)
print(sorted_list)