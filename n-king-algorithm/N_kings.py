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

def n_king(n, kings, colum=0, kings_last_row=np.full(n, -1)):
    if colum >= n:
        return pd.DataFrame(kings)
    for row in range(n):
        if captured_places[row, colum] == 0 and kings_last_row[colum] < row:
            kings[row, colum] = 1
            capture(row, colum)
            kings_last_row[colum] = row
            return n_king(n, kings, colum+1, kings_last_row)
        elif row == n-1:
            kings_last_row[colum] = -1
            colum -= 1
            kings[kings_last_row[colum]] = 0
            capture(kings_last_row[colum], colum, add=False)
            return n_king(n, kings, colum, kings_last_row)

n_king(n, kings)
