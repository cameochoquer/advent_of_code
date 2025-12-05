data = [line.strip() for line in open("1.txt", "r").readlines()]
boundaries = (0, 99)


def split_string(numberstring: str) -> int:
    direction = numberstring[0:1]
    number = int(numberstring[1:])
    if direction == "L":
        return -abs(number)
    return number


def add_numbers(current: int, addition: int) -> int:
    if addition > 0:
        for i in range(addition):
            current += 1
            if current > 99:
                current = 0
    else:
        for i in range(abs(addition)):
            current -= 1
            if current < 0:
                current = 99
    return current


if __name__ == "__main__":
    result = [split_string(numberstring) for numberstring in data]
    zero_count = 0
    moves = [50]
    for move in result:
        new_moves = []
        for next_move in moves:
            position = add_numbers(next_move, move)
            if position == 0:
                zero_count += 1
            new_moves.append(position)
        moves = new_moves

    print(zero_count)
