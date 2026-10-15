def custom_min(collection):
  if not collection:
    raise ValueError("Collection is empty")

  minimum = collection[0]
  for item in collection:
    if item < minimum:
      minimum = item

  return minimum


def custom_sort(collection):
  arr = list(collection)
  n = len(arr)

  for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = True
    if not swapped:
      break

  return arr


my_list = [42, 15, 8, 99, 23, 4]
print("Original list:", my_list)
print("Minimum element:", custom_min(my_list))
print("Sorted list:", custom_sort(my_list))

print("-" * 30)

my_tuple = (10, -3, 55, 0, 12)
print("Original tuple:", my_tuple)
print("Minimum element:", custom_min(my_tuple))
print("Sorted version (as list):", custom_sort(my_tuple))