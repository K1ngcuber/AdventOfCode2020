check_nums = []
remaining_nums = []

with open("door9_input.txt","r") as f:
    for i in range(25):
        check_nums.append(int(f.readline()))
    
    for line in f.readlines():
        remaining_nums.append(int(line))

pc = 0
run = True

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
        print(num)