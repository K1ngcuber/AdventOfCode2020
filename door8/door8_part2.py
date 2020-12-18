instructions = []
history = []
acc = 0
pc = 0
last_pcs = []
change = True
run = True

with open("door8_input.txt","r") as f:
    instructions = list(f.readlines())

def parse_instruction(instruction):
    global pc
    global acc
    global last_pcs
    global change

    instr,arg = instruction.split(" ")

    if instr == "nop" and change and pc not in last_pcs:
        last_pcs.append(pc)
        change = False
        instr = "jmp"
    elif instr == "jmp" and change and pc not in last_pcs:
        last_pcs.append(pc)
        change = False
        instr = "nop"

    if instr == "nop":
        pc += 1
        pass
    elif instr == "acc":
        acc += int(arg)
        pc += 1
    elif instr == "jmp":
        pc += int(arg)


while run:
    if pc in history:
        change = True
        pc = 0
        acc = 0
        history=[]
    elif pc == len(instructions):
        print(acc)
        run = False
    else:
        history.append(pc)
        parse_instruction(instructions[pc])
