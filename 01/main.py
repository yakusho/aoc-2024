sum = 0

with open('input', 'r') as file:
    data = [tuple(map(int, line.split())) for line in file]

sorted_col1 = sorted((num1, idx) for idx, (num1, _) in enumerate(data))
sorted_col2 = sorted((num2, idx) for idx, (_, num2) in enumerate(data))

for i in range(len(data)):
    num1, idx1 = sorted_col1[i]
    num2, idx2 = sorted_col2[i]
    sum += abs(num1 - num2)

print(sum)
