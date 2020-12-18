check_nums = []
remaining_nums = []
all_nums = []

with open("door9_input.txt","r") as f:
    for line in f.readlines():
        all_nums.append(int(line))

check_nums = all_nums[0:25]
remaining_nums = all_nums[25:]

pc = 0
run = True
wrong_num = 0

while run:
    num = remaining_nums[pc]
    found = False
    for a in check_nums:
        for b in check_nums:
            if a+b == num and not found:
                found = True
                check_nums = check_nums[1::]
                check_nums.append(num)
                pc += 1
                continue
        
    if not found:
        run = False
        wrong_num = num

start = 0
count = 0
sequence = []
run = True

while run:
    tmp = 0
    count = 0
    sequence = []
    for i in range(start,len(all_nums)):
        print(i,count,all_nums[i])
        tmp += all_nums[i]
        sequence.append(all_nums[i])
        print(tmp)
        if tmp > wrong_num:
            start += 1
            break
        elif tmp == wrong_num:
            run = False
            break
        count += 1
    print("-"*20)

sequence.sort()
print(sequence[0]+sequence[-1])

