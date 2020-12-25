earliest = 0
time = 0
my_bus = 0
ids = []

with open("door13_input.txt","r") as f:
    earliest = int(f.readline())
    busses = f.readline().split(",")
    for id in busses:
        if id != "x":
            ids.append(int(id))

found = False
time = earliest

while not found:
    print(time,earliest)
    for id in ids:
        if time % id == 0:
            my_bus = id
            found = True
    time += 1
print(time-1-earliest)
print((time -1 - earliest)*my_bus)