from collections import defaultdict
def count_nums(nums: list):
    dict1 = defaultdict(list)
    for n in nums:
        dict1[n].append(n)
    return dict1


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    dict1 = count_nums(nums1)
    dict2 = count_nums(nums2)

    result = []

    for n in dict1.keys():
        if (n in dict2):
            if len(dict1[n]) == len(dict2[n]):
                result += dict1[n]
            else:
                if len(dict1[n]) == min(len(dict1[n]), len(dict2[n])):
                    result += dict1[n]
                else:
                    result += dict2[n]

    
    if result:
        return result



# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# nums1 = [1,2,2,1]
# nums2 = [2]

nums1 = [54,93,21,73,84,60,18,62,59,89,83,89,25,39,41,55,78,27,65,82,94,61,12,38,76,5,35,6,51,48,61,0,47,60,84,9,13,28,38,21,55,37,4,67,64,86,45,33,41]
nums2 = [17,17,87,98,18,53,2,69,74,73,20,85,59,89,84,91,84,34,44,48,20,42,68,84,8,54,66,62,69,52,67,27,87,49,92,14,92,53,22,90,60,14,8,71,0,61,94,1,22,84,10,55,55,60,98,76,27,35,84,28,4,2,9,44,86,12,17,89,35,68,17,41,21,65,59,86,42,53,0,33,80,20]

print(intersect(nums1, nums2))