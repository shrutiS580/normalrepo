arr = [1, 2, 4, 5, 6]
n = 6

expected = n * (n + 1) // 2
actual = 0

for num in arr:
    actual += num

print(expected - actual)