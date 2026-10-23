str1 = "abc"
str2 = "xyz"

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

print(f"""Whe have 2 vars - {str1} and {str2}
After swapping the first 2 characters, we have - {new_str1} and {new_str2}""")