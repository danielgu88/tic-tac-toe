def three_x_row():
    if ((grid[0] == "X" and grid[1] == "X" and grid[2] == "X") or (grid[3] == "X" and grid[4] == "X" and grid[5] == "X")
    or (grid[6] == "X" and grid[7] == "X" and grid[8] == "X") or (grid[0] == "X" and grid[3] == "X" and grid[6] == "X")
    or (grid[1] == "X" and grid[4] == "X" and grid[7] == "X") or (grid[2] == "X" and grid[5] == "X" and grid[8] == "X")
    or (grid[0] == "X" and grid[4] == "X" and grid[8] == "X") or (grid[2] == "X" and grid[4] == "X" and grid[6] == "X")):
        return True

    return False

def three_o_row():
    if ((grid[0] == "O" and grid[1] == "O" and grid[2] == "O") or (grid[3] == "O" and grid[4] == "O" and grid[5] == "O")
    or (grid[6] == "O" and grid[7] == "O" and grid[8] == "O") or (grid[0] == "O" and grid[3] == "O" and grid[6] == "O")
    or (grid[1] == "O" and grid[4] == "O" and grid[7] == "O") or (grid[2] == "O" and grid[5] == "O" and grid[8] == "O")
    or (grid[0] == "O" and grid[4] == "O" and grid[8] == "O") or (grid[2] == "O" and grid[4] == "O" and grid[6] == "O")):
        return True

    return False

def count_x():
    count = 0

    for i in range(9):
        if grid[i] == "X":
            count += 1

    return count

def count_o():
    count = 0

    for i in range(9):
        if grid[i] == "O":
            count += 1

    return count

def count_empty_cells():
    count = 0

    for i in range(9):
        if grid[i] == "_":
            count += 1

    return count

# write your code here
grid = list(input("Enter cells: "))
print("---------")
print("| " + grid[0] + " " + grid[1] + " " + grid[2] + " |")
print("| " + grid[3] + " " + grid[4] + " " + grid[5] + " |")
print("| " + grid[6] + " " + grid[7] + " " + grid[8] + " |")
print("---------")

if ((three_x_row() and three_o_row()) or (abs(count_x() - count_o()) >= 2)):
    print("Impossible")
elif three_x_row():
    print("X wins")
elif three_o_row():
    print("O wins")
elif count_empty_cells() == 0:
    print("Draw")
else:
    print("Game not finished")
