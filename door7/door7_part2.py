import re


posibilities = []
bags = []
result = 0

class Bag:
    def __init__(self,color,amount,children = []):
        self.color = color
        self.amount = int(amount)
        self.children = children

    def __repr__(self):
        return self.color + " " + str(self.amount)

def get_children(bag):
    found_nums = []
    for child in bag.children:
        for b in bags:
            if b.color == child.color:
                found_nums.append([child.amount,get_children(b)])

    return found_nums

def calc_sum(children):
    for child in children:
        if isinstance(child[1],list) and len(child[1]) != 0:
            sum_child = calc_sum(child[1])
            if not isinstance(sum_child,list):
                child[1] = sum_child

    tmp = 0
    for c in children:
        if isinstance(c[1],list):
            tmp += c[0]
        else:
            tmp += c[0] + c[0] * c[1]

    return tmp


instructions = []
bag_color_regex = re.compile(r'^(\w+\s+\w+)')
child_regex = re.compile(r'(\d)\s(\w+\s+\w+)')


with open("door7_input.txt","r") as f:
    instructions = list(f.readlines())

for instruction in instructions:
    bag_color = bag_color_regex.match(instruction).group()
    bag_children = child_regex.findall(instruction)
    children = []
    if bag_children is not None:
        for child in bag_children:
            children.append(Bag(child[1].strip(),child[0]))
    bags.append(Bag(bag_color,1,children))

bag = None
for b in bags:
    if b.color == "shiny gold":
        bag = b


print(calc_sum(get_children(bag)))


