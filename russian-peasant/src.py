def russian_multiply(num1, num2):
    sorted_nums = sorted([num1, num2])
    low, high = sorted_nums[0], sorted_nums[1]
    low_array = []
    high_array = []
    result = 0

    while (low > 1):
        low = int(low / 2)
        low_array.append(low)

        high = high * 2
        high_array.append(high)

    for n in range(0, len(low_array)):
        if (low_array[n] % 2) is not 0:
            result += high_array[n]

    return result
