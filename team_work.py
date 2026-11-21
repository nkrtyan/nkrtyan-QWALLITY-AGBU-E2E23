# task1

number = int(input("Enter your number: "))
for a in range(1,11):
# while a <= 10:
    print(f"{number} * {a} = {number * a}")
    a+=1

# task2
c = int(input("Enter yout number: "))
for b in range(1,c+1):
    for j in range(b):
        print(b, end="")
    print()