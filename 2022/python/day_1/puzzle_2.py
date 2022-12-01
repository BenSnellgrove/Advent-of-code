store = [-1, -1, -1]
inp = ""
cur = 0
temp = 0

while True:

    try:
        inp = input()

        if inp == "stop":

            break


        if inp == "":

            for n in range(3):

                if cur > store[n]:
                    temp = store[n]
                    store[n] = cur
                    cur = temp

            cur = 0

            continue

        cur += int(inp)

    except Exception:
        pass


print(store[0] + store[1] + store[2])
