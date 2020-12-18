passport = ""
passports = []
valid = 0
checks = ['byr','iyr', 'eyr','hgt', 'hcl', 'ecl', 'pid']

with open("door4_input.txt","r") as f:
    for line in f.readlines():
        if(line.strip() == ""):
            passports.append(passport)
            passport = ""
        else:
            passport += line.strip() + " "
    passports.append(passport)

for passport in passports:
    isValid = True
    for check in checks:
        if check not in passport.strip():
            isValid = False
            break
    if isValid: valid += 1

print(valid)