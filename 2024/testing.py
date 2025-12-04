from itertools import groupby

test_list = [
    ("0124", "string"),
    ("1123", "string"),
    ("1223", "string"),
    ("0224", "string"),
    ("0124", "string"),
    ("1123", "string"),
    ("1223", "string"),
    ("0224", "string"),
]

sorted_list = sorted(test_list, key=lambda x: (x[0][2:], x[0][:2]))
# print(sorted_list)

grouped = groupby(sorted_list, key=lambda x: x[0][2:])
# print(grouped)
group_list = [
    (snapshot, len(list(ref)))
    for snapshot, ref in groupby(sorted_list, key=lambda x: x[0])
]
print(group_list)
