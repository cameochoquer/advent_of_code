data = [line.strip().split(",") for line in open("2.txt", "r").readlines()][0]

ids = [item.split("-") for item in data]

numbers = [[int(x) for x in row] for row in ids]

sequences = [list(range(seq[0], seq[1] + 1)) for seq in numbers]


def is_invalid(number: int):
    string = str(number)
    current_numner = 0
    for numb in string:
        if int(number) < current_numner:
            return True
        current_numner = int(number)

    # if len(string) % 2 != 0:
    #     return False
    # mid = len(string) // 2

    # return string[:mid] == string[mid:]


if __name__ == "__main__":
    invalid_ids = []
    for sequence in sequences:
        # print(sequence[0])
        for i in range(sequence[0], sequence[-1] + 1):
            if is_invalid(i):
                invalid_ids.append(i)

    print(sum(invalid_ids))

    # sequence = []
    # print(ids[0])
    # for id in ids[0]:
    #     for x in range(int(id[0]), int(id[1]) + 1):
    #         sequence.append(x)

    # print(sequence)
