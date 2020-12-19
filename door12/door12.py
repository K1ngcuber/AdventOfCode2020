# east  = 0
# south = 1
# west  = 2
# north = 3

facing = 0
x = 0
y = 0

def execute_input(input):
    global x,y,facing
    command = input[0]
    arg = int(input[1::])
    print(command, arg)
    if command == 'N':
        y += arg
    elif command == 'S':
        y -= arg
    elif command == "E":
        x += arg
    elif command == "W":
        x -= arg
    elif command == "L":
        facing = (facing - arg//90) % 4
        print(facing)
    elif command == "R":
        facing = (facing + arg//90) % 4
        print(facing)

    elif command == "F":
        if facing == 0:
            x += arg
        elif facing == 1:
            y -= arg
        elif facing == 2:
            x -= arg
        elif facing == 3:
            y += arg

with open("door12_input.txt","r") as f:
    for line in f.readlines():
        execute_input(line)

print(abs(x) + abs(y))
    