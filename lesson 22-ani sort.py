a = [4, 5, 6, 8, 3, 1]
b = range(len(a))
for j in range(len(a)):
    print(j)
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
a[j]
print(a)
