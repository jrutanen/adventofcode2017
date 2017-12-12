def GetIndexOfMaxValue(list):
    a = -1;
    index = 0
    highestIndex = -1
    for element in list:
        if element > a:
            a = element
            highestIndex = index
        index += 1
    return highestIndex

def DistributeValue(list):
    indexOfMaxValue = GetIndexOfMaxValue(list)
    amountToDistribute = list[indexOfMaxValue]
    index = indexOfMaxValue + 1
    list[indexOfMaxValue] = 0
    for value in range(0, amountToDistribute):
        if index >= len(list):
            index = 0
        list[index] += 1
        index += 1

def DiffBetweenSameValues(list):
    return len(list) - list.index(list[-1]) - 1


def CountRedistributionCycles(banks):
    cycleCount = 0
    startBank = banks[:]
    tempBank = banks[:]
    infiniteLoop = False
    usedAllocations = []
    while not infiniteLoop:
        DistributeValue(tempBank)
        cycleCount += 1
        if tempBank in usedAllocations:
            infiniteLoop = True
            usedAllocations.append(tempBank[:])
        else:
            usedAllocations.append(tempBank[:])

    print("Length of Infinite Loop: " + str(DiffBetweenSameValues(usedAllocations)))
    return cycleCount

puzzleInput = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]

print("Puzzle answer = " + str(CountRedistributionCycles(puzzleInput)))

testBank = [0, 2, 7, 0]
if CountRedistributionCycles(testBank) == 5:
    print("Test Case 1 passed.")
else:
    print("Test Case 1 failed.")