with open("input.txt") as input:
    inputList = input.read().splitlines()

max = 0
idList = []
for line in inputList:
    y = 0
    x = 0
    for i in range(7):
        if line[i] == 'B':
            y += 2**(6-i)
    for i in range(3):
        if line[i+7] == 'R':
            x += 2**(2-i)
    id = 8*y + x
    if id > max:
        max = id
    idList.append(id)
print(max)


seat = [x for x in range(max) if ((x-1) in idList) and ((x+1) in idList) and x not in idList]
print(seat)
