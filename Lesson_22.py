numbers = [7, 2, -5, 13, 24]
min_n = numbers[0]

for item in numbers[1:]:
    if item < min_n:
        min_n = item
print(min_n)



numbers = [9,-6,205,21]
max_n = numbers[0]

for item in numbers[1:]:
    if item > max_n:
        max_n = item
print(max_n)


numbers = [-5,406,37,89]
new_numbers = []

for i in range (len(numbers)):
    min_num = numbers [0]

    for item in numbers:
        if item < min_num:
            min_num = item

new_numbers.append(min_num) 
numbers.remove(min_num)

print(new_numbers)  


      






