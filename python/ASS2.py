arr = [10, 25, 8, 40, 40, 30]

largest = float('-inf')
second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

if second == float('-inf'):
    print("No second largest element")
else:
    print(second)