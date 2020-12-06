with open("input.txt") as input:
    inputList = input.read().split("\n\n")

total = 0
for group in inputList:
    thisGroup = []
    for char in group:
        if char == "\n":
            continue
        if not (char in thisGroup):
            thisGroup.append(char)
    total += len(thisGroup)
print(total)

total = 0
for group in inputList:
    people = group.splitlines()
    thisGroup = list(people[0])
    for person in people:
        tempThisGroup = [x for x in thisGroup]
        for char in thisGroup:
            if not (char in person):
                tempThisGroup.remove(char)
        thisGroup = tempThisGroup
    print(people, len(thisGroup), thisGroup)
    total += len(thisGroup)
print(total)