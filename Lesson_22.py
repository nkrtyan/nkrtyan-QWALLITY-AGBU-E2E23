numbers = [7, 2, -5, 13, 24]

min_n = numbers[0]

for number in numbers:
    if number < min_n:
        min_n = number
print(min_n)


max_n = numbers[0]
for number in numbers:
    if number > max_n:
        max_n = number
print(max_n)


