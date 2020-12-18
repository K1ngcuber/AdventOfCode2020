import re

regex = re.compile(r'(\d+)-(\d+)\s([a-z]):\s(.*)')
correct,min,max = 0,0,0
letter = ''
phrase = ""

with open("door2_input.txt", 'r') as f:
    for line in f.readlines():
        match = regex.findall(line)
        min,max,letter,phrase = match[0]
        min = int(min)-1
        max = int(max)-1
        if max < len(phrase):
            if (phrase[min] == letter or phrase[max] == letter):
                if not (phrase[min] == letter and phrase[max] == letter):
                    correct +=1

print(correct)