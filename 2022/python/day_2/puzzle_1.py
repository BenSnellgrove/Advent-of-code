inp = ""
score = 0

rps = "abc"

while True:

    try:

        inp = input().lower()

        if inp == "":
            break


        inp = inp.replace("x", "a")
        inp = inp.replace("y", "b")
        inp = inp.replace("z", "c")
        inp = inp.split(" ")



        # What we play
        score += (rps.index(inp[1]) % 3) + 1


        # draw case
        if inp[0] == inp[1]:
            score+= 3
            continue

        # 2 special cases then simple <> checks
        if inp[0] == "c" and inp[1] == "a":
            score+= 6
            continue


        if inp[0] == "a" and inp[1] == "c":
            continue



        # normal cases
        if inp[0] < inp[1]:
            score+= 6
            continue

    except Exception:
        pass


print(score)
