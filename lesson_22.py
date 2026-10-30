nums =input("Enter Numbers: ").split()

max_num = nums[0]
min_num = nums[0]

for num in nums:
    if num > max_num:
        max_num = num
       
for num in nums:
    if num < min_num:
        min_num = num
        
for i in range(len(nums)):
    for j in range(0, len(nums) - i -1):
        if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp
        
print(f'Min : {min_num},\n Max: {max_num},\nSort: {nums}')      