with open("input.txt") as input:
    inputList = input.read().splitlines()
    numValid1 = 0
    numValid2 = 0
    for i in inputList:
        pair = tuple(i.split(": "))
        a = pair[0].split(" ")
        b = a[0].split("-")
        pair = ((int(b[0]), int(b[1]), a[1]), pair[1])
        passNum = pair[1].count(pair[0][2])
        if passNum >= pair[0][0] and passNum <= pair[0][1]:
            numValid1 += 1
        if (pair[1][pair[0][0]-1] == pair[0][2]) ^ (pair[1][pair[0][1]-1] == pair[0][2]):
            numValid2 += 1
    print(numValid1)
    print(numValid2)
