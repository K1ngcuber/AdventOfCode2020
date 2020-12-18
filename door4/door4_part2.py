import re

passport = ""
passports = []
valid = 0
checks = ['byr','iyr', 'eyr','hgt', 'hcl', 'ecl', 'pid']
eye_color = ['amb','blu','brn','gry','grn','hzl','oth']

def heightCheck(value):
    regex = re.compile(r'\d+')
    num = int(regex.match(value).group())
    if 'cm' in value:
        if num >= 150 and num <= 193:
            return True
    elif 'in' in value:
        if num >= 59 and num <=76:
            return True
    return False

def checkHair(value):
    regex = re.compile(r'#[0-9a-f]')
    return regex.match(value)

def checkPid(value):
    regex = re.compile(r'[0-9]{9}')
    return regex.match(value) is not None


with open("door4_input.txt","r") as f:
    for line in f.readlines():
        if(line.strip() == ""):
            passports.append(passport)
            passport = ""
        else:
            passport += line.strip() + " "
    passports.append(passport)

with open("test",'w') as output:

    for passport in passports:
        isValid = True
        data = dict(map(lambda x: x.split(":") ,passport.strip().split(" ")))
        
        for key in checks:
            if key not in data.keys():
                isValid = False
                break
        if isValid:
            if not (data['byr'].isdigit() and int(data['byr']) >= 1920 and int(data['byr']) <= 2002):
                isValid = False
            if not (data['iyr'].isdigit() and int(data['iyr']) >= 2010 and int(data['iyr']) <= 2020):
                isValid = False
            if not (data['eyr'].isdigit() and int(data['eyr']) >= 2020 and int(data['eyr']) <= 2030):
                isValid = False
            if not heightCheck(data['hgt']):
                isValid = False
            if not checkHair(data['hcl']):
                isValid = False
            if not data['ecl'] in eye_color:
                isValid = False
            if not checkPid(data['pid']):
                isValid = False
            
        if isValid:
            output.write(str(data) + '\n')
            output.write(str(isValid) + "\n")
            valid += 1

    print(valid)