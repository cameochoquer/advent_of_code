import re

data = [line.strip() for line in open("input3.txt", "r").readlines()]

print(type(data))
newstring = ""
for x in data:
    newstring += "" + x

# print(newstring)
res = 0
muls = re.findall(r"mul\(\d+,\d+\)", newstring)
for mul in muls:
    string_tuple = mul.replace("mul", "")
    new_tuple = eval(string_tuple)
    res += new_tuple[0] * new_tuple[1]

print(res)
