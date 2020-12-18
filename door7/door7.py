import re

posibilities = []

class Bag:
    def __init__(self,color,amount,children = []):
        self.color = color
        self.amount = amount
        self.children = children

    def __repr__(self):
        return self.color + " " + str(self.amount)

def find_posibilities(color):
    for bag in bags:
        for child in bag.children:
            if child.color == color:
                posibilities.append(bag.color)
                find_posibilities(bag.color)

instructions = []
bag_color_regex = re.compile(r'^(\w+\s+\w+)')
child_regex = re.compile(r'(\d)\s(\w+\s+\w+)')
bags = []

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

find_posibilities("dark violet")
result = []

for posibility in posibilities:
    if posibility not in result:
        result.append(posibility)

print(len(result))

