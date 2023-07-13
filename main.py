import time

start = time.time()

sudoku_raw = [
    [5, 3, 0, 0, 0, 4, 7, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 3, 0],
    [0, 0, 0, 3, 6, 0, 0, 0, 1],

    [6, 7, 0, 0, 1, 0, 0, 4, 9],
    [0, 0, 0, 9, 0, 6, 0, 0, 0],
    [4, 5, 0, 0, 8, 0, 0, 2, 6],

    [2, 0, 0, 0, 7, 9, 0, 0, 0],
    [0, 6, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 1, 4]
]

normal_line = (1, 2, 3, 4, 5, 6, 7, 8, 9)


def take_a_row(raw: list, y: int):
    return raw[y]


def take_a_column(raw: list, x: int):
    return [i[x] for i in raw]


def take_a_square(raw: list, num_index: int, num_of_row: int):
    x1 = 0
    x2 = 0
    x3 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    if num_of_row in (0, 1, 2):
        y1, y2, y3 = 0, 1, 2
    elif num_of_row in (3, 4, 5):
        y1, y2, y3 = 3, 4, 5
    elif num_of_row in (6, 7, 8):
        y1, y2, y3 = 6, 7, 8

    if num_index in (0, 1, 2):
        x1, x2, x3 = 0, 1, 2
    elif num_index in (3, 4, 5):
        x1, x2, x3 = 3, 4, 5
    elif num_index in (6, 7, 8):
        x1, x2, x3 = 6, 7, 8

    result = [raw[y1][x1], raw[y1][x2], raw[y1][x3],
              raw[y2][x1], raw[y2][x2], raw[y2][x3],
              raw[y3][x1], raw[y3][x2], raw[y3][x3]]

    return result


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
possible_numbers = []

finish = 1

while finish > 0:
    finish = len([a for a in sudoku_raw if int(a.count(0)) > 0])

    for row_index, row in enumerate(sudoku_raw):  # итерация по строкам судоку

        possible_numbers = [a for a in numbers if a not in row]
        if len(possible_numbers) == 1:
            row[row.index(0)] = possible_numbers[0]

        for pos_num in possible_numbers:  # итерация по возможным номерам

            row_dict = {0: False, 1: False, 2: False,
                        3: False, 4: False, 5: False,
                        6: False, 7: False, 8: False}

            for item_index, item in enumerate(row):  # итерация по строке

                if item != 0:
                    pass
                elif item == 0:
                    if pos_num not in take_a_square(sudoku_raw, item_index, row_index) and \
                            pos_num not in take_a_row(sudoku_raw, row_index) and \
                            pos_num not in take_a_column(sudoku_raw, item_index):
                        row_dict[item_index] = True

            if list(row_dict.values()).count(True) == 1:
                row[get_key(row_dict, True)] = pos_num
            else:
                pass

print(*sudoku_raw, sep="\n")

end = time.time() - start
print(end)
