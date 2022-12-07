class FileTree():
    def __init__(self, name):
        self.name = name
        self.subdirs = []
        self.value = 0

    def treebor(self):

        if len(self.subdirs) == 0:
            return self.value

        for subdir in self.subdirs:

            self.value += subdir.treebor()


        return self.value

    def treeborTWO(self):
        seen.append(self.value)
        for sub in self.subdirs:
            sub.treeborTWO()


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
stack[0].treeborTWO()
diff = stack[0].value - 40000000


seen.sort()

for s in seen:
    if s < diff:
        continue
    else:
        print(s)
        break
