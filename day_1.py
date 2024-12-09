right_numbers = []
left_numbers = []

with open("input.txt") as f:
    for line in f:
        left, right = line.split("   ")
        left_numbers.append(int(left))
        right_numbers.append(int(right))

total = 0
for left_num in left_numbers:
    count = right_numbers.count(left_num)
    score = left_num * count
    total += score
print(total)

# right_numbers.sort()
# left_numbers.sort()
# # distance = sum(abs(left - right) for left, right in zip(left_numbers, right_numbers))
24931009
