#sorting in descending order
def descending_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


#sorting in ascending order
def ascending_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr




array = [1, 4, 33, 455]
print(descending_bubble_sort(array))
print(ascending_bubble_sort(array))


