print('1 Write a Python program to get the Fibonacci series between 0 to 50.\n')

first_el = 0
second_el = 1

while first_el <= 50:
    print(first_el,end =" ")
    temp = first_el
    first_el = second_el
    second_el = temp + second_el


print("\n")
print('2 Write a Python program that accepts a string and calculates the number of digits and letters.\n')  

Data = "Python 3.13"
Letters = 0
Digits = 0

for i in Data:
    if i.isalpha():
        Letters += 1
    elif i.isdigit():
        Digits += 1
print(f"Letters: {Letters} and Digits: {Digits}\n")   

print("3 Write a Python program to print alphabet pattern 'L'\n")

for i in range(7):
  row =""
  for j in range(5):
    if j == 0 or i == 6:
      row += "*"
    else:
      pass
  print(row) 


