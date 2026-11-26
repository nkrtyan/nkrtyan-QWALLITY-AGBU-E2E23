
numbers = list(map(int , input("Enter any numbers use spaces").split()))

min_valeu = numbers[0] 
for x in numbers:
    if x < min_valeu:
     min_valeu = x
print(min_valeu, 'min value')



numbers2 = numbers.copy()
sortNumbers = []
while len(numbers2) > 0:
      sortNumbers.append(min(numbers2))
      numbers2.remove(min(numbers2))
print(sortNumbers, 'sortNumbers list' )














