# def addBinary(a: str, b: str) -> str:
#     n = 0
#     i = min(len(a), len(b)) - 1
#     mappings = {'11': ('0', True), '10': ('1', False),
#                 '01': ('1', False), '00': ('0', False)}
#     result = ''
#     carry_on = ''
#     while (n < len(a) and n < len(b)):

#         bsum = mappings[b[i] + a[i]]

#         if carry_on:
#             bsum = mappings[bsum[0] + carry_on]
#             carry_on = ''

#         if bsum[1]:
#             carry_on = '1'

#         result = bsum[0] + result
#         i -= 1
#         n += 1

#     if carry_on:
#         result = addBinary(result, carry_on)

#     return result
#     result = carry_on + result

# return result


# print(addBinary('11', '1'))

# Think of a recursive solution instead of the mess above
# def sumBin(b1: str, b2: str):
#     if int(b1) + int(b2) == 2:
#         return '10'

#     return str(int(b1) + int(b2))


# def addBinary(a: str, b: str) -> str:
#     stackA = [bit for bit in a]
#     stackB = [bit for bit in b]
#     stackC = []
#     result = ''
#     while (stackA and stackB):
#         n1 = stackA.pop()
#         n2 = stackB.pop()
#         carry = None
#         if stackC:
#             carry = stackC.pop()

#         bsum = sumBin(n1, n2)

#         while len(bsum) > 1:
#             stackC.append(bsum[0])
#             if carry:
#                 bsum = sumBin(bsum[1], carry)
#             else:
#                 result


#         else:
#             result += bsum

#     while (stackB):
#         carry_on_leftover = stackB.pop()
#         result += carry_on_leftover

#     return result[::-1]  # Reverse the string to get the correct order


# print(addBinary('1010', '1011'))
