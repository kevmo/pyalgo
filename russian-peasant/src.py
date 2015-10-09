def russian_multiply(num1, num2):
    """Verbose."""
    sorted_nums = sorted([num1, num2])
    low, high = sorted_nums[0], sorted_nums[1]
    low_array = [low]
    high_array = [high]
    result = 0

    while (low > 1):
        low, toss = divmod(low, 2)
        low_array.append(low)

        high = high * 2
        high_array.append(high)

    for n in range(0, len(low_array)):
        if (low_array[n] % 2):
            result += high_array[n]

    return result


def bit_russian(num1, num2):
    """Solved using bit shifting."""
    x, y = num1, num2
    z = 0

    while x > 0:
        if x % 2: z = z + y
        x = x >> 1
        y = y << 1

    return z
