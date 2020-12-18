instructions = []
history = []
acc = 0
pc = 0
run = True

with open("door8_input.txt","r") as f:
    instructions = list(f.readlines())

def parse_instruction(instruction):
    global pc
    global acc
    instr,arg = instruction.split(" ")
    if instr == "nop":
        pc += 1
        pass
    elif instr == "acc":
        acc += int(arg)
        pc+=1
    elif instr == "jmp":
        pc += int(arg)

while run:
    print(instructions[pc])
    if pc in history:
        print(acc)
        run = False
    else:
        history.append(pc)
        parse_instruction(instructions[pc])
