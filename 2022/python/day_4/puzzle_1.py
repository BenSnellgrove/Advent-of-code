
# check if 1 lies within 2
def check(thingy):
    if thingy[0][0] >= thingy[1][0] and thingy[0][0] <= thingy[1][1]:
        if thingy[0][1] >= thingy[1][0] and thingy[0][1] <= thingy[1][1]:
            return True
    return False


inp = ""
count = 0

while True:

    try:

        inp = input()

        if inp == "":
            break

        inp = inp.split(",")

        for i in range (2):
            inp[i] = inp[i].split("-")

        for i in range(2):
            for j in range(2):
                inp[i][j] = int(inp[i][j])

        if check(inp):
            count += 1
            continue


        temp = inp[0]
        inp[0] = inp[1]
        inp[1] = temp

        if check(inp):
            count += 1
            continue



    except Exception:
        pass


print(count)
