import numpy as np

sudoku_raw = np.array([[0, 9, 0, 0, 5, 0, 3, 4, 0],
                       [1, 4, 0, 6, 0, 0, 8, 0, 0],
                       [0, 0, 0, 8, 0, 1, 0, 0, 0],

                       [0, 0, 0, 0, 3, 0, 0, 6, 9],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [8, 2, 0, 0, 1, 0, 0, 0, 0],

                       [0, 0, 0, 3, 0, 4, 0, 0, 0],
                       [0, 0, 6, 0, 0, 9, 0, 7, 5],
                       [0, 8, 2, 0, 6, 0, 0, 3, 0]
                       ])


# sudoku_raw = np.array([
#     [5, 3, 0, 0, 0, 4, 7, 0, 0],
#     [0, 0, 0, 0, 0, 7, 0, 3, 0],
#     [0, 0, 0, 3, 6, 0, 0, 0, 1],
#
#     [6, 7, 0, 0, 1, 0, 0, 4, 9],
#     [0, 0, 0, 9, 0, 6, 0, 0, 0],
#     [4, 5, 0, 0, 8, 0, 0, 2, 6],
#
#     [2, 0, 0, 0, 7, 9, 0, 0, 0],
#     [0, 6, 0, 5, 0, 0, 0, 0, 0],
#     [0, 0, 3, 6, 0, 0, 0, 1, 4]
# ])


def take_np_column(raw, x: int):
    return raw[:, x]


def take_a_row(raw, y: int):
    return raw[y]


def square(raw, x, y):
    x1 = 0
    x2 = 0
    x3 = 0
    y1 = 0
    y2 = 0
    y3 = 0

    def assign_index(n):
        if n in (0, 1, 2):
            return 0, 1, 2
        elif n in (3, 4, 5):
            return 3, 4, 5
        elif n in (6, 7, 8):
            return 6, 7, 8

    x1, x2, x3 = assign_index(x)
    y1, y2, y3 = assign_index(y)

    result = [(raw[y1][x1], y1, x1), (raw[y1][x2], y1, x2), (raw[y1][x3], y1, x3),
              (raw[y2][x1], y2, x1), (raw[y2][x2], y2, x2), (raw[y2][x3], y2, x3),
              (raw[y3][x1], y3, x1), (raw[y3][x2], y3, x2), (raw[y3][x3], y3, x3)
              ]

    return result


def take_pos_numbers(square_output):
    list_of_numbers = [i[0] for i in square_output if i[0] != 0]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = [i for i in numbers if i not in list_of_numbers]
    return result


def check_on_zeros(raw):
    for i in raw:
        if np.count_nonzero(i == 0) > 0:
            return True
        else:
            return False


sqrs = [(0, 0), (3, 0), (6, 0),
        (0, 3), (3, 3), (6, 3),
        (0, 6), (3, 6), (6, 6)]

f = 1000

while f > 0:

    f -= 1

    for s in sqrs:
        sqr = square(sudoku_raw, s[0], s[1])
        possible_numbers = take_pos_numbers(sqr)
        for pos_num in possible_numbers:
            counter = 0
            ry = 0
            rx = 0
            for num, y, x in sqr:
                if num != 0:
                    continue
                if pos_num not in take_a_row(sudoku_raw, y) and \
                        pos_num not in take_np_column(sudoku_raw, x):
                    counter += 1
                    ry = y
                    rx = x
            if counter == 1:
                sudoku_raw[ry][rx] = pos_num

print(sudoku_raw)
