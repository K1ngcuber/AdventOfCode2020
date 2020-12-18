numbers = []
diffs = {
    1:0,
    2:0,
    3:0,
}
last_num = 0

with open("door10_input.txt","r") as f:
    numbers = list(map(int, f.readlines()))

numbers.sort()

for n in numbers:
    diffs[n-last_num] += 1
    last_num = n

diffs[3] += 1

print(diffs)

print(diffs[1] * diffs[3])
