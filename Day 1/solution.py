with open("input.txt") as input:
    inputList = input.read().splitlines()
    for i in range(len(inputList)):
        inputList[i] = int(inputList[i])
    
    for i in inputList:
        if inputList.count(2020 - i) > 0:
            print(f"{i} * {2020 - i} = {i*(2020 - i)}")
    
    for i in inputList:
        remainder = 2020 - i
        for j in inputList:
            if inputList.count(remainder - j) > 0:
                print(f"{i} * {j} * {remainder - j} = {i*j*(remainder-j)}")
