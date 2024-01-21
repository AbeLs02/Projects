import numpy as np
import pandas as pd
# n = int(input("enter n:"))
n = 8
kings = np.zeros((n, n), dtype=int)
captured_places = np.zeros((n, n), dtype=int)


def capture(row, colum, direction=None, add=True):
    if (not 0 <= row < len(kings)) or (not 0 <= colum < len(kings)):
        return
    if add:
        captured_places[row, colum] += 1
    else:
        captured_places[row, colum] -= 1
    if direction == "t":
        capture(row - 1, colum, "t", add)
    elif direction == "b":
        capture(row + 1, colum, "b", add)
    elif direction == "tl":
        capture(row - 1, colum - 1, "tl", add)
    elif direction == "tr":
        capture(row - 1, colum + 1, "tr", add)
    elif direction == "r":
        capture(row, colum - 1, "r", add)
    elif direction == "l":
        capture(row, colum + 1, "l", add)
    elif direction == "bl":
        capture(row + 1, colum - 1, "bl", add)
    elif direction == "br":
        capture(row + 1, colum + 1, "br", add)
    else:
        if add:
            captured_places[row, colum] = -1
        else:
            captured_places[row, colum] = 0
        capture(row - 1, colum, "t", add)
        capture(row + 1, colum, "b", add)
        capture(row - 1, colum - 1, "tl", add)
        capture(row - 1, colum + 1, "tr", add)
        capture(row, colum - 1, "r", add)
        capture(row, colum + 1, "l", add)
        capture(row + 1, colum - 1, "bl", add)
        capture(row + 1, colum + 1, "br", add)

def n_king(n):
    colum = 0
    king_row = np.zeros(n, dtype=int)

    while colum < n:
        for row in range(n):
            if captured_places[row, colum] == 0 and kings[row, colum] == 0:
                kings[row, colum] = 1
                capture(row, colum)
                king_row[colum] = row
                colum += 1
                break
            elif row == n-1:
                kings[:, colum:] = 0
                colum -= 1
                kings[king_row[colum], colum] = -1
                capture(king_row[colum], colum, add=False)
            else:
                kings[row, colum] = -1

    # print(king_row)
    print(kings)
    kings[kings == -1] = 0
    print(kings)
    print(captured_places)
    print(pd.DataFrame(kings))

    print('----------------')

n_king(n)
