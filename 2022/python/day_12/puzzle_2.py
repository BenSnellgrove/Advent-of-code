heights = "SabcdefghijklmnopqrstuvwxyzEL"
heights = "EzyxwvutsrqponmlkjihgfedcbaSL"

# can drop massively
# can only go up 1


class Point:
    def __init__(self, val, location, dist):
        self.value = val
        self.distance = dist
        self.location = location

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __gt__(self, other):
        return self.distance > other.distance



map = []

queue = []


inp = ""

while True:

    inp = input()

    if inp == "":
        break

    temp = []
    for i in inp:
        temp.append(i)

    map.append(temp)


map2 = map
all = []
for i in map2:
    for j in i:
        all.append(j)

print(all)

for h in heights:
    if all.count(h) == 1:
        print(h,end="")
        print(all.index(h))


def trav(x,y, path):

    print(path)

    if [x,y] in path:
        return False

    path.append([x,y])

    if map[x][y] == "E":
        return path

    if x - 1 >= 0:
        if not trav(x - 1, y, path):
            return path

    if x + 1 <= len(map):
        if not trav(x + 1, y, path):
            return path

    if y - 1 >= 0:
        if not trav(x, y - 1, path):
            return path

    if y + 1 <= len(map[0]):
        if not trav(x, y + 1, path):
            return path

    path.remove([x,y])

    return False




queue.append(Point("E", [20, 138], 0))

end = None

while len(queue) != 0:

    queue.sort()
    cur = queue[0]

    queue.reverse()
    queue.pop()
    queue.reverse()

    if cur.value == "a":
        end = cur
        break

    if cur.location[0] - 1 >= 0:
        if heights.index(map[cur.location[0] - 1][cur.location[1]]) <= heights.index(cur.value) + 1:
            queue.append(Point(
                map[cur.location[0] - 1][cur.location[1]],
                [cur.location[0] - 1, cur.location[1]],
                cur.distance + 1
            ))
            map[cur.location[0] - 1][cur.location[1]] = "L"

    if cur.location[0] + 1 < len(map):
        if heights.index(map[cur.location[0] + 1][cur.location[1]]) <= heights.index(cur.value) + 1:
            queue.append(Point(
                map[cur.location[0] + 1][cur.location[1]],
                [cur.location[0] + 1, cur.location[1]],
                cur.distance + 1
            ))
            map[cur.location[0] + 1][cur.location[1]] = "L"

    if cur.location[1] - 1 >= 0:
        if heights.index(map[cur.location[0]][cur.location[1] - 1]) <= heights.index(cur.value) + 1:
            queue.append(Point(
                map[cur.location[0]][cur.location[1] - 1],
                [cur.location[0], cur.location[1] - 1],
                cur.distance + 1
            ))
            map[cur.location[0]][cur.location[1] - 1] = "L"

    if cur.location[1] + 1 < len(map[0]):
        if heights.index(map[cur.location[0]][cur.location[1] + 1]) <= heights.index(cur.value) + 1:
            queue.append(Point(
                map[cur.location[0]][cur.location[1] + 1],
                [cur.location[0], cur.location[1] + 1],
                cur.distance + 1
            ))
            map[cur.location[0]][cur.location[1] + 1] = "L"





print(end.distance)

# print(trav(0, 0, []))
# print(trav(20, 0, []))


