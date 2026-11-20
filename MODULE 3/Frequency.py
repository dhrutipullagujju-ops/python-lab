numbers = [1, 2, 3, 2, 1, 2, 4, 3]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Frequency of elements:")

for key, value in frequency.items():
    print(key, ":", value)
