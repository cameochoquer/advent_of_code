# BREADTH_FIRST_SEARCH


def find_word(grid, target):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    rows = len(grid)
    cols = len(grid[0])

    def check_direction(row, col, x, y):
        word = ""
        current_row = row
        current_col = col
        positions = []

        while (
            0 <= current_row < rows
            and 0 <= current_col < cols
            and len(word) < len(target)
        ):
            word += grid[current_row][current_col]
            positions.append((current_row, current_col))
            current_row += x
            current_col += y
        return word == target, positions

    found = []
    for row in range(rows):
        for col in range(cols):
            for x, y in directions:
                is_match, positions = check_direction(row, col, x, y)
                if is_match:
                    found.append(positions)
    return found


target = "XMAS"
grid = [line.strip() for line in open("input4.txt", "r").readlines()]

matches = find_word(grid, target)
print(len(matches))
