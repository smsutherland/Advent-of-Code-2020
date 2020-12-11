with open("input.txt") as input:
    inputList = [int(x) for x in input.read().splitlines()]

prev25 = []
errorNum = 0
for i in inputList[:25]:
    prev25 = prev25 + [i]

for i in inputList[25:]:
    for j in prev25:
        diff = i - j
        if diff in prev25:
            break
    else:
        errorNum = i
        break    
    prev25 = prev25[1:] + [i]
print(errorNum)

for i in range(len(inputList)):
    for j in range(i+1, len(inputList)):
        if sum(inputList[i:j + 1]) == errorNum:
            print(max(inputList[i:j + 1]) + min(inputList[i:j + 1]))
            break
