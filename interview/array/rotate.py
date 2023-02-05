def rotate(nums: list[int], k: int) -> None:
    temp = nums.copy()
    for i in range(len(nums)):
        nums[(i+k) % len(nums)] = temp[i]
    
    """
    Do not return anything, modify nums in-place instead.
    """
nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)