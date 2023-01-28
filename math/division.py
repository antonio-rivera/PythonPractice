def divide(dividend: int, divisor: int) -> int:
    if dividend + divisor == 0:
        return -1
    elif abs(dividend + divisor) == 2 * dividend:
        return 1

    negative = False
    if divisor < 0:
        divisor = -divisor
        negative = not negative

    if dividend < 0:
        negative = not negative
        dividend = -dividend

    quot = len(range(dividend-divisor, -1, -divisor))

    if quot >= 2**31 and negative:
        quot = 2**31

    elif quot > 2**31 - 1:
        quot = 2**31 - 1

    return quot if negative is False else -quot


# print(divide(-2147483648, 1))
# # print(divide(48, -2))
