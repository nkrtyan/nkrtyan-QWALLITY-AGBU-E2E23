num_count=int(input("Input number "))

for i in range(1,11):
    result=num_count*i
    print(f" {num_count} x {i} 8=", result)


for i in range(1,row_num+1):
    print (i)
    for j in range(i):
        print(j ,end=" ")
