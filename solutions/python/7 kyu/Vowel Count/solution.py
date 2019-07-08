def getCount(inputStr):
    return sum(c in "aeiou" for c in inputStr)