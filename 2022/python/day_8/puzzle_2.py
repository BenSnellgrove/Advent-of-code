trees = []
inp = []
temp = []
bestScore = 0

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

        if x == 0 or y == 0 or x == len(trees) - 1 or y == len(trees[0]) - 1:
            continue


        score = 1
        count = 0

        # 1 direction
        for n in range(x):
            count += 1
            if trees[x - n - 1][y] >= trees[x][y]:
                score *= count
                count = 0
                break
        if count != 0:
            score *= count

        count = 0
        for n in range(x + 1, len(trees)):
            count += 1
            if trees[n][y] >= trees[x][y]:
                score *= count
                count = 0
                break
        if count != 0:
            score *= count

        count = 0
        for n in range(y):
            count += 1
            if trees[x][y - n - 1] >= trees[x][y]:
                score *= count
                count = 0
                break#
        if count != 0:
            score *= count

        count = 0
        for n in range(y + 1, len(trees[0])):
            count += 1
            if trees[x][n] >= trees[x][y]:
                score *= count
                count = 0
                break
        if count != 0:
            score *= count

        if score > bestScore:
            bestScore = score







print(bestScore)
