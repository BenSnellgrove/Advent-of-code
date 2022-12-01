prev = -1
inp = ""
cur = 0

while True:

    try:
        inp = input()

        if inp == "stop":

            break


        if inp == "":
            if cur > prev:
                prev = cur

            cur = 0

            continue

        cur += int(inp)

    except Exception:
        pass


print(prev)
