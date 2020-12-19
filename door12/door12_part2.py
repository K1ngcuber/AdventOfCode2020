# east  = 0
# south = 1
# west  = 2
# north = 3

waypoint_x = 10
waypoint_y = 1
facing = 0
x = 0
y = 0

def execute_input(input):
    global x,y,facing,waypoint_y,waypoint_x
    command = input[0]
    arg = int(input[1::])
    if command == 'N':
        waypoint_y += arg
    elif command == 'S':
        waypoint_y -= arg
    elif command == "E":
        waypoint_x += arg
    elif command == "W":
        waypoint_x -= arg
    elif command == "L":
        for i in range(arg//90):
            newY = waypoint_x
            newX = waypoint_y * -1
            waypoint_y = newY
            waypoint_x = newX

    elif command == "R":

        for i in range((360-arg)//90):
            newY = waypoint_x
            newX = waypoint_y * -1
            waypoint_y = newY
            waypoint_x = newX

    elif command == "F":
        for i in range(arg):
            x += waypoint_x
            y += waypoint_y


    print("ship",x,y)
    print("point",waypoint_x,waypoint_y)

with open("door12_input.txt","r") as f:
    for line in f.readlines():
        execute_input(line)

print(abs(x) + abs(y))
    