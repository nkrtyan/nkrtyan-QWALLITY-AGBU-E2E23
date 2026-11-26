# 1. Write a Python program to get the Fibonacci series between 0 to 50. 
# Expected Output : 0 1 1 2 3 5 8 13 21 34

# myList = [0, 1 ]
# maxNumber = int(input('Enter number '))
# while myList[-1] + myList[-2]<= maxNumber:
#    myList.append(myList[-1] + myList[-2])   
# print(myList)

# 2. Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data: Python 3.13
# Expected Output:
# Letters 6
# Digits 3

# sampleData = 'Python 3.13' 

# letters = sum(1 for x in sampleData if x.isalpha())
# print('Letters', letters)
# digits = sum(1 for x in sampleData if x.isdigit())
# print('Digits', digits)

# letters=0
# digits=0

# for x in sampleData:
#     if x.isalpha():
#         letters += 1
#     elif x.isdigit():
#         digits += 1
# print('Letters', letters)
# print('Digits', digits)

#3. Write a Python program to print alphabet pattern 'L'  
# Expected Output:
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *****

# star = '*'
# for x in range(6):
#     print(star)
# print(star*5)



# 1
# 22
# 333
# 4444

numbers = range(1,10)

for i in numbers:
    for j in numbers:
        if j <= i:
            print(i ,end ='')
    print()



         



