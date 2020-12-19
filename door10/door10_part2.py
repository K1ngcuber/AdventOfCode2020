from collections import defaultdict


numbers = []
diffs = {
    1:0,
    2:0,
    3:0,
}
last_num = 0
counts = defaultdict(int, {0: 1})


with open("door10_input.txt","r") as f:
    numbers = list(map(int, f.readlines()))

numbers.sort()
numbers.append(numbers[-1]+3)

for n in numbers:
    diffs[n-last_num] += 1
    last_num = n
    counts[n] = counts[n-3]+counts[n-2]+counts[n-1]

print(diffs)
print(counts)
