mask = ""
addresses = []
memory = {}

def apply_mask(arg):
    for x,index in zip(mask,range(len(mask))):
        if x != 'X':
            arg[index] = x
    return arg

def bit_to_int(bit_array):
    integer = 0
    bit_array.reverse()
    for i,index in zip(bit_array,range(len(bit_array))):
        if i == 1:
            integer += 2**index
    return integer

with open("door14_input.txt", "r") as f:
    for line in f.readlines():
        operation,arg = line.strip().split(" = ")
        if operation == "mask":
            mask = [int(x) if x != 'X' else 'X' for x in arg]
        elif "mem" in operation:
            address = operation.replace("mem","").replace("[","").replace("]","")
            bit_arg = [int(x) if x != " " else 0 for x in '{0:36b}'.format(int(arg))]
            memory[address] = bit_to_int(apply_mask(bit_arg))

print(sum(memory.values()))