def containsDuplicate(nums: list[int]) -> bool:
    num_count = {}

    for n in nums:
        if n in num_count:
            num_count[n] += 1
        else:
            num_count[n] = 1
    max_count = max(num_count.values())
    return max_count > 1

nums = [1,2,3,4]

print(containsDuplicate(nums))