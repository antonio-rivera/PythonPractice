def plusOne(digits: list[int]) -> list[int]:
    n = len(digits) - 1
    new_digits = add(digits, n)
    if new_digits[0] == 0:
        new_digits = [1] + new_digits
    
    return new_digits



def add(digits, idx):
    if idx >= 0:
        if digits[idx] == 9:
            digits[idx] = 0
            add(digits, idx-1)

        else:
            digits[idx] += 1

    return digits
    

# idx = 0
#  0  1   
# [9, 9] -> [1, 0, 0]
# [1, 3, 9]

# digits = [1,2,3]
# digits = [4,3,2,1]
# digits = [9]
# digits = [9, 9, 9, 9, 9, 9]

digits = [1, 2, 9, 9]

print(plusOne(digits))