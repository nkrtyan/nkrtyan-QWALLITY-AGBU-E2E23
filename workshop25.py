#1
number = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#2
for i in range(1,10):
    for j in range(i):
        print(i, end="")
    print("\n", end ="")
   