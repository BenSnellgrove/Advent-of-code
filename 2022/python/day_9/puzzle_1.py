inp = ""
score = 0

head = [0, 0]
tail = [0, 0]

visited = []

while True:

    try:

        inp = input()

        if inp == "":
            break

        inp = inp.split(" ")

        for i in range(int(inp[1])):

            if inp[0] == "U":
                head[0] += 1

            if inp[0] == "D":
                head[0] -= 1

            if inp[0] == "L":
                head[1] -= 1

            if inp[0] == "R":
                head[1] += 1

            if abs(head[0] - tail[0]) > 1:
                tail[0] = int( head[0] - ((head[0] - tail[0]) / 2) )
                tail[1] = head[1]

            elif abs(head[1] - tail[1]) > 1:
                tail[1] = int( head[1] - ((head[1] - tail[1]) / 2) )
                tail[0] = head[0]

            _tail = "" + str(tail[0]) + " " + str(tail[1])

            if _tail not in visited:
                visited.append(_tail)





    except Exception:
        pass

print(len(visited))
