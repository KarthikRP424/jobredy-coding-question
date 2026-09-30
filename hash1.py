n = [1, 2, 3, 4, 5, 6, 77, 7, 77, 89, 9]

m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 1, 4, 5, 6, 7, 8, 9]

frequency_map = {}

for num in m:
    count = 0

    for x in n:
        if num == x:
            count += 1

    frequency_map[num] = count


print(frequency_map)