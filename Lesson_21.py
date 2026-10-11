age = int(input("How old are you? \n"))
decade = age // 10
year = age % 10
if year == 0:
    print(f"You are {decade} decades old")
else:
    print(f"You are {decade} decades and {year} years old")
#TODO, add also case when user input not number
# Nel, working code