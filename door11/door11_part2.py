import copy

board = []
board_copy = []

def check_around(i,j):
    neighbors = []
    for jj in range(j-1,-1,-1):
        if board[i][jj] != ".":
            neighbors.append(board[i][jj])
            break
    for jj in range(j+1,len(board[i])):
        if board[i][jj] != ".":
            neighbors.append(board[i][jj])
            break

    for ii in range(i-1,-1,-1):
        if board[ii][j] != ".":
            neighbors.append(board[ii][j])
            break
    for ii in range(i+1,len(board)):
        if board[ii][j] != ".":
            neighbors.append(board[ii][j])
            break
    
    for ii,jj in zip(range(i-1,-1,-1),range(j-1,-1,-1)):
        if board[ii][jj] != ".":
            neighbors.append(board[ii][jj])
            break
    for ii,jj in zip(range(i+1,len(board)),range(j-1,-1,-1)):
        if board[ii][jj] != ".":
            neighbors.append(board[ii][jj])
            break
    for ii,jj in zip(range(i-1,-1,-1),range(j+1,len(board[i]))):
        if board[ii][jj] != ".":
            neighbors.append(board[ii][jj])
            break
    for ii,jj in zip(range(i+1,len(board)),range(j+1,len(board[i]))):
        if board[ii][jj] != ".":
            neighbors.append(board[ii][jj])
            break

    occupied = neighbors.count("#")
    if board[i][j] == "L":
        if occupied == 0:
            return "#"
        else:
            return "L"
    elif board[i][j] == "#":
        if occupied >= 5:
            return "L"
        else:
            return "#"

with open("door11_input.txt","r") as f:
    for line in f.readlines():
        board.append([])
        for letter in line.strip():
            board[len(board)-1].append(letter)

run = True
while run:
    board_copy = copy.deepcopy(board)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                continue
            else:
                board_copy[i][j] = check_around(i,j)
    if board == board_copy:
        run = False
        break
    board = board_copy

occupied = 0
for row in board:
    occupied += row.count("#")

print(occupied)