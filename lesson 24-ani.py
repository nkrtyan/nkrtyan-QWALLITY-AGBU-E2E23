# a=0
# b=1
# while a<= 50:
#     print(a, end=" ")
#     a, b = b, a + b

# text =input("enter a string:")
# letters=0
# digits=0
# for item in text:
#     if item.isalpha():
#          letters +=1
#     elif item.isdigit():
#         digits +=1
# print(letters)
# print(digits)

for a in range(5):
    for b in range(5):
        if b==0 or a==4:
            print("*", end=" ")
        else:
            print( " ", end=" ")
            print()
