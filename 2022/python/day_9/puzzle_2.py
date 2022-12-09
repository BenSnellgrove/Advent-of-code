inp = ""
score = 0

body = []
for i in range(10):
    body.append([0, 0])

visited = []

while True:

    try:

        inp = input()

        if inp == "":
            break

        inp = inp.split(" ")

        for n in range(int(inp[1])):

            if inp[0] == "U":
                body[0][0] += 1

            if inp[0] == "D":
                body[0][0] -= 1

            if inp[0] == "L":
                body[0][1] -= 1

            if inp[0] == "R":
                body[0][1] += 1

            for i in range(1, 10):

                head = body[i - 1]
                tail = body[i]

                # diagonal movement
                if abs(head[0] - tail[0]) > 1 and abs(head[1] - tail[1]) > 1:
                    tail[0] = int(head[0] - ((head[0] - tail[0]) / 2))
                    tail[1] = int(head[1] - ((head[1] - tail[1]) / 2))

                elif abs(head[0] - tail[0]) > 1:
                    tail[0] = int(head[0] - ((head[0] - tail[0]) / 2))
                    tail[1] = head[1]

                elif abs(head[1] - tail[1]) > 1:
                    tail[1] = int(head[1] - ((head[1] - tail[1]) / 2))
                    tail[0] = head[0]

                body[i - 1] = head
                body[i] = tail

            _tail = "" + str(body[9][0]) + " " + str(body[9][1])

            if _tail not in visited:
                visited.append(_tail)

    except Exception:
        pass


print(len(visited))
