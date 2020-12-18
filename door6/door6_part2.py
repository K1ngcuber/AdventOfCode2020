import string

forms = []
answers = []
tmp = []
groups = 0
group_count = 0
sum = 0

with open("door6_input.txt","r") as f:
    forms = list(f.readlines())


for form in forms:
    if form == "\n":
        answers.append((group_count,tmp))
        group_count = 0
        tmp = []
        continue
    else:
        group_count += 1
        groups += 1

    for letter in form:
        if letter != "\n":
            tmp.append(letter)

answers.append((group_count,tmp))


for pair in answers:
    for letter in string.ascii_lowercase:
        
        if pair[0] == pair[1].count(letter):
            sum+=1

print(sum)
