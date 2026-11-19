# Create code that print the max value without using the max() function.
numbers = input("Enter numbers: ").split()
max_value = int(numbers[0])
for item in numbers[1:]:
    if int(item) > max_value:
        max_value = int(item)
print(max_value)

# Create code that print the min value without using the min() function.
numbers = input("Enter numbers: ").split()
min_value = int(numbers[0])
for item in numbers[1:]:
    if int(item) < min_value:
        min_value = int(item)
print(min_value)

# Create code that sort the numbers in ascending order without using the sort() function.
numbers = input("Enter numbers: ").split()
count = 0
for item in numbers:
    count += 1
i = 0
while i < count:
    numbers[i] = int(numbers[i])
    i += 1
i = 0
while i < count:
    j = 0
    while j < count - 1:
        if numbers[j] > numbers[j + 1]:
            trans = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = trans
        j += 1
    i += 1
print(numbers)