grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
count = 0
marker = ""
final_message = ""

def three_x_row():
    global final_message
    if ((grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X") or (grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X")
    or (grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X") or (grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X")
    or (grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X") or (grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X")
    or (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or (grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X")):
        final_message = "X wins"
        return True

    return False

def three_o_row():
    global final_message
    if ((grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O") or (grid[1][0] == "O" and grid[1][1] == "O" and grid[1][2] == "O")
    or (grid[2][0] == "O" and grid[2][1] == "O" and grid[2][2] == "O") or (grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O")
    or (grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O") or (grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O")
    or (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or (grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O")):
        final_message = "O wins"
        return True

    return False

def draw():
    global final_message
    if not three_x_row() and not three_o_row() and count_empty_cells() == 0:
        final_message = "Draw"
        return True

    return False

# def count_x():
#     count = 0
#
#     for i in range(9):
#         if grid[i] == "X":
#             count += 1
#
#     return count
#
# def count_o():
#     count = 0
#
#     for i in range(9):
#         if grid[i] == "O":
#             count += 1
#
#     return count

def count_empty_cells():
    count = 0

    for i in range(3):
        for j in range(3):
            if grid[i][j] == "_":
                count += 1

    return count

def split_if_possible(move):
    if len(move.split(" ")) == 2:
        return move.split(" ")
    else:
        return [move, ""]

def empty_spaces():
    global grid
    empty_spaces = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == "_":
                empty_spaces.append([i, j])

    return empty_spaces

def numbers(row, column):
    possible_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return row in possible_numbers and column in possible_numbers

def one_to_three(row, column):
    possible_numbers = ["1", "2", "3"]
    return row in possible_numbers and column in possible_numbers

def is_valid_move(row, column):
    valid_move = False

    row -= 1
    column -= 1

    for empty_space in empty_spaces():
        if row == empty_space[0] and column == empty_space[1]:
            valid_move = True
            break

    return valid_move

def print_grid():
    global grid
    print("---------")
    print("| " + grid[0][0] + " " + grid[0][1] + " " + grid[0][2] + " |")
    print("| " + grid[1][0] + " " + grid[1][1] + " " + grid[1][2] + " |")
    print("| " + grid[2][0] + " " + grid[2][1] + " " + grid[2][2] + " |")
    print("---------")

def game_over():
    if three_x_row() or three_o_row() or draw():
        return True

    return False

# user_input = input("Enter cells: ")
# grid.append(list(user_input[0:3]))
# grid.append(list(user_input[3:6]))
# grid.append(list(user_input[6:9]))

print_grid()

# if ((three_x_row() and three_o_row()) or (abs(count_x() - count_o()) >= 2)):
#     print("Impossible")
# elif three_x_row():
#     print("X wins")
# elif three_o_row():
#     print("O wins")
# elif count_empty_cells() == 0:
#     print("Draw")
# else:
#     print("Game not finished")

while not game_over():
    move = split_if_possible(input("Enter the coordinates: "))

    valid_move = False

    while not valid_move:
        if numbers(move[0], move[1]):
            if one_to_three(move[0], move[1]):
                if is_valid_move(int(move[0]), int(move[1])):
                    if count % 2 == 0:
                        marker = "X"
                    else:
                        marker = "O"

                    grid[int(move[0]) - 1][int(move[1]) - 1] = marker
                    valid_move = True
                    count += 1

                else:
                    print("This cell is occupied! Choose another one!")
                    move = split_if_possible(input("Enter the coordinates: "))

            else:
                print("Coordinates should be from 1 to 3!")
                move = split_if_possible(input("Enter the coordinates: "))

        else:
            print("You should enter numbers!")
            move = split_if_possible(input("Enter the coordinates: "))

    print_grid()

print(final_message)
