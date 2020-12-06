with open("input.txt") as input:
    inputList = input.read().splitlines()

neededCreds = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

numValid = 0
gottenCreds = {}
for line in inputList:
    if line == "":
        valid = True
        for a in neededCreds:
            if a not in gottenCreds.keys():
                valid = False
        for a in gottenCreds.keys():
            cred = gottenCreds[a]
            if a == "byr":
                if len(cred) != 4:
                    valid = False
                if not (1920 <= int(cred) <= 2002):
                    valid = False
            if a == "iyr":
                if len(cred) != 4:
                    valid = False
                if not (2010 <= int(cred) <= 2020):
                    valid = False
            if a == "eyr":
                if len(cred) != 4:
                    valid = False
                if not (2020 <= int(cred) <= 2030):
                    valid = False
            if a == "hgt":
                if cred[-2:] == "cm":
                    if not (150 <= int(cred[:-2]) <= 193):
                        valid = False
                elif cred[-2:] == "in":
                    if not (59 <= int(cred[:-2]) <= 76):
                        valid = False
                else:
                    valid = False
            if a == "hcl":
                if cred[0] != "#":
                    valid = False
                for letter in cred[1:]:
                    if letter not in "0123456789abcdef":
                        valid = False
            if a == "ecl":
                if cred not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    valid = False
            if a == "pid":
                if len(cred) != 9:
                    valid = False
                for letter in cred:
                    if letter not in "0123456789":
                        valid = False

        if valid:
            numValid += 1
        gottenCreds = {}
    creds = line.split(" ")
    for cred in creds:
        cred1 = cred[0:3]
        if cred1 in neededCreds:
            gottenCreds[cred1] = cred[4:]
        
print(numValid)

