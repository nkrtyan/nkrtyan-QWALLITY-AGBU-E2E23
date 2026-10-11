age = input("How old are you? \n")
if age.isdigit() == False:
    print("Please enter a number for your age")
else:       
    age_number = int(age)    
    decade = age_number // 10
    year = age_number % 10
    if year == 0:
        print(f"You are {decade} decades old")
    else:
        print(f"You are {decade} decades and {year} years old")
        
# fixed, add also case when user input not number
# Nel, working code