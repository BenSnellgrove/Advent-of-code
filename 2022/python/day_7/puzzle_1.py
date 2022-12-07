
class FileTree():
    def __init__(self, name):
        self.name = name
        self.subdirs = []
        self.value = 0

    def treebor(self):


        if len(self.subdirs) == 0:
            return self.value


        for subdir in self.subdirs:

            temp = subdir.treebor()
            self.value += temp


        return self.value

    def treeborTWO(self):
        c = 0
        if len(self.subdirs) == 0 and self.value <= 100000:
            return self.value
        for subdir in self.subdirs:
             c += subdir.treeborTWO()
        if self.value <= 100000:
            c += self.value

        return c





seen = []
inp = []
stack = []
cur = None
out = 0
curDir = ""

while True:


    inp = input()

    if inp == "":
        break

    if inp.startswith("$ cd .."):



        stack[-2].subdirs.append(cur)
        cur = stack[-2]

        stack = stack[:-1]

        continue
    elif inp.startswith("$ cd"):
        stack.append(FileTree(inp.split(" ")[2]))
        if len(stack) > 1:
            stack[-2] = cur
        cur = stack[-1]

    try:
        cur.value += int(inp.split(" ")[0])
    except Exception:
        pass


while len(stack) > 1:
    stack[-2].subdirs.append(cur)
    cur = stack[-2]

    stack = stack[:-1]



stack[0].treebor()
print(stack[0].treeborTWO())
