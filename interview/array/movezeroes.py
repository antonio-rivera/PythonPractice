def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def moveZeroes(nums: list[int]) -> None:
    for i in range(len(nums)-1):
        j = i + 1 
        # for j in range(i+1, len(nums)):
        if nums[i] == 0 and nums[j] != 0:
            pos = i
            while(pos >= 0 and nums[pos] == 0):
                pos -= 1
            swap(nums, pos+1, j)


# [0, 0, 0, 3]
# [0, 1, 0, 3, 12] -> [1, 0, 0, 3, 12] -> []
# nums = [0, 1, 0, 3, 12]
# nums = [0, 0, 0, 3]
# nums = [0, 1, 2, 3, 4, 0]
nums = [0, 0, 0, -2, -10]

moveZeroes(nums)

print(nums)