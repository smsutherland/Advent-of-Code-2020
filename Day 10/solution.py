with open("input.txt") as input:
    inputList = [int(x) for x in input.read().splitlines()]


def isValid(adapters):
    for i in range(len(adapters) - 1):
        cur = adapters[i]
        nex = adapters[i+1]
        dif = nex - cur
        if dif > 3:
            return False
    return True

def removeElement(list, index):
    if index == len(list):
        return list[:-1]
    return list[:index] + list[index + 1:]

def calculatePossibilities(length):
    print(length)
    if length == 0:
        return 1
    if length == 1:
        return 1
    if length == 2:
        return 2
    length += 1
    testList = range(length)
    thesePossibilities = 0
    for i in range(2**(length - 2)):
        binary = bin(i)[2:]
        newList = [0]
        newList += [testList[i] for i, char in zip(range(1, length - 1), binary) if binary[i-1] == "1"]
        newList += [length - 1]
        if isValid(newList):
            thesePossibilities += 1
    return thesePossibilities

difDist = {1: 0, 2: 0, 3: 0}
inputList.sort()
inputList = [0] + inputList + [max(inputList) + 3]
possibilities = 1
num1s = 0
for i in range(len(inputList) - 1):
    cur = inputList[i]
    nex = inputList[i+1]
    dif = nex - cur
    difDist[dif] += 1
    if dif == 1:
        num1s += 1
    else:
        possibilities *= calculatePossibilities(num1s)
        num1s = 0

difDist[3] += 1
print(difDist[1] * difDist[3])
print(possibilities)

#386869246296064