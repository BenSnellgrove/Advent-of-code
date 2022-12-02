inp = ""
score = 0

rps = "abc"

while True:

    try:

        inp = input().lower()

        if inp == "":
            break


        inp = inp.split(" ")


        if inp[1] == "x":
            score += ((rps.index(inp[0]) + 2) % 3) + 1

        if inp[1] == "y":
            score += 3
            score += (rps.index(inp[0]) % 3) + 1

        if inp[1] == "z":
            score += 6
            score += ((rps.index(inp[0]) + 1) % 3) + 1



    except Exception:
        pass


print(score)
