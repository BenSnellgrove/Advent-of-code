trees = []
inp = []
temp = []
count = 0

while True:

    inp = input()

    if inp == "":
        break

    temp = []
    for c in inp:
        temp.append(int(c))

    trees.append(temp)



for x in range(len(trees)):
    for y in range(len(trees[0])):

        if x == 0 or y == 0:
            count += 1
            continue

        if x == len(trees) - 1 or y == len(trees[0]) - 1:
            count += 1
            continue

        seen = [True] * 4

        # 1 direction
        for n in range(x):
            if trees[n][y] >= trees[x][y]:
                seen[0] = False
                break

        for n in range(x + 1, len(trees)):
            if trees[n][y] >= trees[x][y]:
                seen[1] = False
                break

        for n in range(y):
            if trees[x][n] >= trees[x][y]:
                seen[2] = False
                break

        for n in range(y + 1, len(trees[0])):
            if trees[x][n] >= trees[x][y]:
                seen[3] = False
                break

        if any(seen):
            count += 1






print(count)
