with open("input.txt") as input:
    inputList = input.read().splitlines()

bags = {}
for line in inputList:
    line = line[:-1]
    theseBags = line.split(" contain ")
    contains = theseBags[1].split(", ")
    contains = [x[2:] for x in contains]
    if contains == [" other bags"]:
        contains = []
    for i in range(len(contains)):
        if contains[i][-1] != 's':
            contains[i] = contains[i] + "s"
        
    bags[theseBags[0]] = contains
#print(bags)

def canContain(bag):
    if "shiny gold bags" in bags[bag]:
        return True
    for nextBag in bags[bag]:
        if canContain(nextBag):
            return True
    return False

totalNum = 0
for bag in bags.keys():
    if canContain(bag):
        totalNum += 1
print(totalNum)

bags = {}
for line in inputList:
    line = line[:-1]
    theseBags = line.split(" contain ")
    contains = theseBags[1].split(", ")
    if contains == ["no other bags"]:
        contains = []
    print(contains)
    for i in range(len(contains)):
        if contains[i][-1] != 's':
            contains[i] = contains[i] + "s"
        
    bags[theseBags[0]] = contains

def numContained(bag):
    contained = bags[bag]
    total = 0
    for i in contained:
        num = int(i[0:1])
        bagName = i[2:]
        total += num * (numContained(bagName)+1)
    return total

print(numContained("shiny gold bags"))