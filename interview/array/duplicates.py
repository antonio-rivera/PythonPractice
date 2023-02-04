# nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [0,1,2,3]
# nums = [0,1,1,2,2]
def removeDuplicates(nums):
    k = 0
    i = 0
    while(i < len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] != nums[j]:
                k += 1
                i += 1
                if i < len(nums):
                    nums[i] = nums[j]
        return k + 1
        


nums = [1,1,2]
print(removeDuplicates(nums))
print(nums)