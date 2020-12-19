import copy

board = []
board_copy = []

def check_around(i,j):
    neighbors = []
    occupied = 0
    for ii in range(max(0,i-1),min(i+2,len(board))):
        for jj in range(max(0,j-1),min(j+2,len(board[ii]))):
            if (ii,jj) == (i,j):
                continue
            neighbors.append(board[ii][jj])
    occupied = neighbors.count("#")
    if board[i][j] == "L":
        if occupied == 0:
            return "#"
        else:
            return "L"
    elif board[i][j] == "#":
        if occupied >= 4:
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