data = [line.strip() for line in open("input2.txt", "r").readlines()]

# part one:
# count = 0
# for string in data:
#     string_list = string.split(" ")
#     number_list = [int(num) for num in string_list]
#     ascending = all(
#         number_list[i] < number_list[i + 1] for i in range(len(number_list) - 1)
#     )
#     descending = all(
#         number_list[i] > number_list[i + 1] for i in range(len(number_list) - 1)
#     )
#     delta_check = all(
#         abs(number_list[i] - number_list[i + 1]) <= 3
#         for i in range(len(number_list) - 1)
#     )
#     if not (ascending or descending) or not delta_check:
#         print("unsafe")
#     else:
#         count += 1
#         print(number_list)

# print(count)


def check_report(report):
    dict = {}
    ascending = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    descending = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    delta_check = all(
        abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1)
    )
    if not (ascending or descending) or not delta_check:
        dict["unsafe"] = report
    else:
        dict["safe"] = report
    return dict


def check_new_report(report):
    ascending = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    descending = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    delta_check = all(
        abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1)
    )
    if not (ascending or descending) or not delta_check:
        return None
    else:
        return report


# part 2:
count = 0
results = []
unsafe = []

for string in data:
    string_list = string.split(" ")
    number_list = [int(num) for num in string_list]
    safety_dict = check_report(number_list)
    if "unsafe" in safety_dict:
        for i in range(len(number_list)):
            test_list = number_list[:i] + number_list[i + 1 :]
            result = check_new_report(test_list)
            if result is not None:
                count += 1
                break

print(count + 411)
print(len(results))
# print(len(unsafe) + 411)


# new_list = [check_new_report(value[:i] + value[i + 1 :]) for i in range(len(value))]
# check_level = check_report(new_list)
# ascending = all(
#     number_list[i] < number_list[i + 1] for i in range(len(number_list) - 1)
# )
# descending = all(
#     number_list[i] > number_list[i + 1] for i in range(len(number_list) - 1)
# )
# delta_check = all(
#     abs(number_list[i] - number_list[i + 1]) <= 3 for i in range(len(number_list) - 1)
# )
# if not (ascending or descending) or not delta_check:
#     print("unsafe")
# else:
#     count += 1


# print(count)
