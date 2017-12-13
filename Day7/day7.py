class ProgramFile:
    name = ""
    weight = 0
    children = []
    parent = 0
    directory = False
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def IsDirectory(self):
        return self.directory

    def SetToDirectory(self):
        self.directory = True

    def GetName(self):
        return self.name

    def GetWeight(self):
        return self.weight

    def SetParent(self, parent):
        self.parent = parent

    def GetParent(self):
        return self.parent

    def AddChild(self, child):
        self.children.append(child)

def CreateObjectList(list):
    objectList = []
    tempList = list[:]
    for item in tempList:
        name = item[:str(item).find(" ")]
        weight = item[str(item).find("(") + 1:str(item).find(")")]
        x = ProgramFile(name, weight)
        objectList.append(x)

        if str(item).find("->") != -1:
            x.SetToDirectory()
    return objectList

def CreateProgramTree(listOfPrograms):
    programList = CreateObjectList(listOfPrograms)[:]
    programs = listOfPrograms[:]
    hasChildren = False
    for item in programs:
        if str(item).find("->") != -1:
            hasChildren = True
            parentName = item[:str(item).find(" ")]
            item = item[str(item).find("->") + 3:]
            while hasChildren == True:
                if str(item).find(",") != -1:
                    childName = item[:str(item).find(",")]
                    item = item[str(item).find(",") + 2:]
                else:
                    hasChildren = False
                    childName = str(item)
                #find child object and update parent
                for node in programList:
                    if node.GetName() == childName:
                        node.SetParent(parentName)
                        #find parent and add child
                        for parent in programList:
                            if parent.GetName() == parentName:
                                parent.AddChild(node)
    return programList

def FindParent(list):
    for item in list:
        if item.GetParent() == 0:
            return item.GetName()

def GetBottomProgram(listOfPrograms):
    tempList = listOfPrograms[:]
    tree = CreateProgramTree(tempList)
    bottomFileName = FindParent(tree)
    return bottomFileName

test_input = [
    "pbga (66)",
    "xhth (57)",
    "ebii (61)",
    "havc (66)",
    "ktlj (57)",
    "fwft (72) -> ktlj, cntj, xhth",
    "qoyq (66)",
    "padx (45) -> pbga, havc, qoyq",
    "tknk (41) -> ugml, padx, fwft",
    "jptl (61)",
    "ugml (68) -> gyxo, ebii, jptl",
    "gyxo (61)",
    "cntj (57)"]

if GetBottomProgram(test_input) == "tknk":
    print("Test Case 1 passed")
else:
    print("Test Case 1 failed")

with open('input.txt', 'r') as puzzle_file:
    puzzle_input = puzzle_file.read()

input = []
for row in puzzle_input.split("\n"):
    input.append(row)

print("Puzzle result is: " + GetBottomProgram(input))
