# . air
# # wall
# o sand


grid = []
for n in range(1000):
    temp = []
    for m in range(200):
        temp.append(".")
    grid.append(temp)


prev = None
inp = ""

while True:

    prev = None

    inp = input()

    if inp == "":
        break

    for i in inp.split(" -> "):
        c = i.split(",")
        c[0] = int(c[0])
        c[1] = int(c[1])

        if prev == None:
            prev = c
            continue

        print("line from ", prev, c)
        for x in range(int(min(prev[0], c[0])), int(max(prev[0], c[0])) + 1):
            for y in range(int(min(prev[1], c[1])), int(max(prev[1], c[1])) + 1):
                print(x,y, end=" ")
                grid[x][y] = "#"

        prev = c


start = [500,0]
pos = start


while True:

    if pos[1] > 198:
        break

    if grid[pos[0]][pos[1] + 1] == ".":
        pos[1] += 1

    elif grid[pos[0] - 1][pos[1] + 1] == ".":
        pos[0] -= 1
        pos[1] += 1

    elif grid[pos[0] + 1][pos[1] + 1] == ".":
        pos[0] += 1
        pos[1] += 1

    else:


        grid[pos[0]][pos[1]] = "o"
        pos = [500,0]

        for n in range(len(grid)):
            if n > 490 and n < 510:
                print(grid[n][0:20])





count = 0

for i in grid:
    count += i.count("o")

for n in range(len(grid)):
    if n >490 and n < 510:
        print(grid[n][0:20])

print(count)
