import math


def uniquePaths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    else:
        return uniquePaths(m-1, n) + uniquePaths(m, n-1)


# print(uniquePaths(2, 3))
# print(uniquePaths(3, 7))


def iterUniquePaths(m, n):
    recursive_stack = [(m, n)]
    total = 0
    while (recursive_stack):
        r, c = recursive_stack.pop()

        if r == 1 or c == 1:
            total += 1

        else:
            recursive_stack.append((r, c-1))
            recursive_stack.append((r-1, c))

    return total


# for i in range(1, 10):
#     for j in range(1, 10):
#         with open(f'{i}-sequence2.txt', 'a') as file:
#             file.write(f"{iterUniquePaths(j, i)} <-- {(j, i)}\n")


def mathUniquePaths(m, n):
    N = (m + n) - 2
    K = m - 1

    return math.comb(N, K)
