import re

data = [line.strip() for line in open("input3.txt", "r").readlines()]

print(type(data))
newstring = ""
for x in data:
    newstring += "" + x

# print(newstring)
res = 0
don = re.findall(r"don\'t\(\)", newstring)
dos = re.findall(r"do\(\)", newstring)
# muls = re.findall(r"mul\(\d+,\d+\)", newstring)
new = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", newstring)
print(new)

# for mul in muls:
#     string_tuple = mul.replace("mul", "")
#     new_tuple = eval(string_tuple)
#     res += new_tuple[0] * new_tuple[1]

new_list = []
dont_list = []
pattern = r"mul\(\d+,\d+\)"

enabled = True
for value in new:
    if value == "do()":
        enabled = True
    elif value == "don't()":
        enabled = False
    elif re.match(pattern, value):
        if enabled:
            string_tuple = value.replace("mul", "")
            new_tuple = eval(string_tuple)
            res += new_tuple[0] * new_tuple[1]
print(res)
