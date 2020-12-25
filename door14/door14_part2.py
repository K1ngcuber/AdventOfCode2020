import itertools
mask = ""
addresses = []
memory = {}

def apply_mask(arg):
    for x,index in zip(mask,range(len(mask))):
        if x != 0:
            arg[index] = x
    indices = [index if x == "X" else None for x,index in zip(arg,range(len(arg)))]

    indices = [x for x in indices if x is not None]

    combinations = list(itertools.product([0, 1], repeat=len(indices)))
    args = []
    for c in combinations:
        tmp = arg.copy()
        for i,j in zip(indices,range(len(indices))):
            tmp[i] = c[j]
        args.append(tmp)
    return args

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
            addresses = apply_mask([int(x) if x != " " else 0 for x in '{0:36b}'.format(int(address))])
            print(len(addresses))
            for adr in addresses:
                memory[bit_to_int(adr)] = int(arg)



result = sum(memory.values())

print(result)