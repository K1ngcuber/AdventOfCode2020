import re

regex = re.compile(r'(\d+)-(\d+)\s([a-z]):\s(.*)')
correct,min,max = 0,0,0
letter = ''
phrase = ""

with open("door2_input.txt", 'r') as f:
    for line in f.readlines():
        match = regex.findall(line)
        min,max,letter,phrase = match[0]
        print(min,max,letter,phrase)
        num = phrase.count(letter)
        if(num >= int(min) and num <= int(max)):
            correct += 1

print(correct)