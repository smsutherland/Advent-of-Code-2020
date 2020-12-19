with open("input.txt") as input:
    ruleList, inputList = input.read().split("\n\n")

# input = """42: 9 14 | 10 1
# 9: 14 27 | 1 26
# 10: 23 14 | 28 1
# 1: "a"
# 11: 42 31
# 5: 1 14 | 15 1
# 19: 14 1 | 14 14
# 12: 24 14 | 19 1
# 16: 15 1 | 14 14
# 31: 14 17 | 1 13
# 6: 14 14 | 1 14
# 2: 1 24 | 14 4
# 0: 8 11
# 13: 14 3 | 1 12
# 15: 1 | 14
# 17: 14 2 | 1 7
# 23: 25 1 | 22 14
# 28: 16 1
# 4: 1 1
# 20: 14 14 | 1 15
# 3: 5 14 | 16 1
# 27: 1 6 | 14 18
# 14: "b"
# 21: 14 1 | 1 14
# 25: 1 1 | 1 14
# 22: 14 14
# 8: 42
# 26: 14 22 | 1 20
# 18: 15 15
# 7: 14 5 | 1 21
# 24: 14 1

# abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaaaabbaaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# babaaabbbaaabaababbaabababaaab
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""
# ruleList, inputList = input.split("\n\n")





def parseRules(rules):
    parsedRules = {}
    for rule in rules:
        num, rule = rule.split(": ")
        if '"' in rule:
            rule = rule[1]
            parsedRules[int(num)] = rule
        else:
            options = rule.split(" | ")
            for i, option in enumerate(options):
                options[i] = [int(x) for x in option.split()]
            parsedRules[int(num)] = options
    return parsedRules

def followsRule(line, ruleNum, rules):
    thisRule = rules[ruleNum]
    if type(thisRule) == str:
        if len(line) > 0:
            if line[0] == thisRule:
                return (True, 1)
            else:
                return (False, 0)
        else:
            print(line, thisRule)
            return (False, 0)
    for ruleSet in thisRule:
        testStr = line
        numRemoved = 0
        for rule in ruleSet:
            result = followsRule(testStr[numRemoved:], rule, rules)
            if result[0]:
                numRemoved += result[1]
            else:
                break
        else:
            return (True, numRemoved)
    return (False, 0)

def matchesZero(line):
    result = followsRule(line, 0, rules)
    result = result[1] == len(line) and result[0]
    return result


rules = parseRules(ruleList.splitlines())

print(len([True for x in inputList.splitlines() if matchesZero(x)]))

def followsRule2(line, ruleNum, rules, depth = 0):
    thisRule = rules[ruleNum]
    if type(thisRule) == str:
        if len(line) > 0:
            if line[0] == thisRule:
                return (True, 1)
            else:
                return (False, 0)
        else:
            return (False, 0)

    if ruleNum == 8 or ruleNum == 11:
        ruleToUse = 0 if depth > 0 else 1
        testStr = line
        numRemoved = 0
        for rule in thisRule[ruleToUse]:
            result = followsRule2(testStr[numRemoved:], rule, rules, depth-1)
            if result[0]:
                numRemoved += result[1]
            else:
                break
        else:
            return (True, numRemoved)
    
    if ruleNum == 0:
        for i in range(10):
            for j in range(10):
                testStr = line
                numRemoved = 0
                result = followsRule2(testStr[numRemoved:], 8, rules, i)
                if result[0]:
                    numRemoved += result[1]
                    result = followsRule2(testStr[numRemoved:], 11, rules, j)
                    if result[0]:
                        numRemoved += result[1]
                        if len(testStr) == numRemoved:
                            return (True, numRemoved)
        return (False, 0)

    else:
        for ruleSet in thisRule:
            testStr = line
            numRemoved = 0
            for rule in ruleSet:
                result = followsRule2(testStr[numRemoved:], rule, rules)
                if result[0]:
                    numRemoved += result[1]
                else:
                    break
            else:
                return (True, numRemoved)
        return (False, 0)

def matchesZero2(line):
    result = followsRule2(line, 0, rules)
    result = result[1] == len(line) and result[0]
    return result

rules[8] = [[42, 8], [42]]
rules[11] = [[42, 11, 31], [42, 31]]

print(len([True for x in inputList.splitlines() if matchesZero2(x)]))
