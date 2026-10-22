base_tupl = (0, 1, 1)
print(f"Fill the Fibonacci sequence. {base_tupl}")
continue_tupl =  tuple(map(int, input(f" ").split()))
full_sequence = base_tupl + continue_tupl
is_correct = True

for item in range(len(full_sequence) - 2):
    if full_sequence[item] + full_sequence[item + 1] != full_sequence[item + 2]:
        is_correct = False
        break
if is_correct:
    print(f"The full Fibonacci sequence after appending numbers in tuple is: {full_sequence}")
else:
    print("Try again :(")