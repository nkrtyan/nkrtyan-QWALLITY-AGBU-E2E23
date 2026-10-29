# code for Fibonacci series

fibonacci_series=[0,1]
x=0
y=1

while x+y<=50:
    z=x+y
    fibonacci_series.append(z)
    x=y
    y=z

print("fibanachi series: ", fibonacci_series)
       
#A loop for counting the letters and digits in the text
sample_data= "python 3.13"
letters=0
digits=0
for i in sample_data:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digits+=1
print("letters:",letters, "\n" "digits:", digits)

#Outputting the letter L
x="*"
for i in range(6):
    print (x)
print (5*x)

