class Monkey:

    def __init__(self, items, operation, test, throws):
        self.items = items
        self.inspects = 0
        self.operation = operation
        self.test = test
        self.monkeys = throws

    def round(self):
        for i in range(len(self.items)):
            self.inspect(i)

        for item in self.items:
            self.throw(self.monkeys[0 if item % self.test == 0 else 1], item)


        self.items = []




    def inspect(self, index):
        self.inspects += 1
        temp = self.items[index]
        temp = self.operation(temp)
        temp //= 3
        self.items[index] = temp



    def throw(self, monkey, item):
        monkeys[monkey].items.append(item)




monkeys = []


monkeys.append(Monkey([65,78], (lambda a: a * 3), 5, [2,3]))
monkeys.append(Monkey([54,78, 86, 79, 73, 64, 85, 88], (lambda a: a + 8), 11, [4,7]))
monkeys.append(Monkey([69,97,77,88,87], (lambda a: a + 2), 2, [5,3]))
monkeys.append(Monkey([99], (lambda a: a + 4), 13, [1,5]))
monkeys.append(Monkey([60,57,52], (lambda a: a * 19), 7, [7,6]))
monkeys.append(Monkey([91,82,85,73,84,53], (lambda a: a + 5), 3, [4,1]))
monkeys.append(Monkey([88,74,68,56], (lambda a: a * a), 17, [0,2]))
monkeys.append(Monkey([54,82,72,71,53,99,67], (lambda a: a + 1), 19, [6,0]))


for n in range(20):
    for m in range(8):
        monkeys[m].round()


for m in monkeys:
    print(m.items)


temp = []
for m in monkeys:
    temp.append(m.inspects)
temp.sort()
temp.reverse()
print(temp)

print(temp[0] * temp[1])
