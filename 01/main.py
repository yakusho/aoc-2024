import bisect

with open('input', 'r') as file:
    data = [tuple(map(int, line.split())) for line in file]

sorted_col1 = sorted([x[0] for x in data])
sorted_col2 = sorted([x[1] for x in data])

def part_1():
    sum = 0

    for i in range(len(data)):
        sum += abs(sorted_col1[i] - sorted_col2[i])
        
    print(f"Part 1: {sum}")

def part_2():
    sum = 0
    track = 1

    for index, x in enumerate(sorted_col1):
        if index + 1 < len(sorted_col1) and sorted_col1[index + 1] == x:
            track += 1
            continue

        left_index = bisect.bisect_left(sorted_col2, x)
        right_index = bisect.bisect_right(sorted_col2, x)
        occurrences = right_index - left_index
        sum += (track * (occurrences * x))
        track = 1
    
    print(f"Part 2: {sum}")

part_1()
part_2()