forms = []
answers = []
sum = 0

with open("door6_input.txt","r") as f:
    forms = list(f.readlines())

answers.append([])
for form in forms:
    if form == "\n":
        answers.append([])
        continue
    for letter in form:
        if letter not in answers[len(answers)-1] and letter != "\n":
            answers[len(answers)-1].append(letter)

for answer in answers:
    sum += len(answer)

print(sum)