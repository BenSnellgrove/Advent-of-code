inp = ""

sigs = []

cycles = 0
register = 1



screen = []





while True:

    try:

        inp = input()

        if inp == "":
            break

        inp = inp.split(" ")

        if len(inp) == 1:
            cycles += 1

            if int(cycles % 40) == register or int(cycles % 40) == register +1 or int(cycles % 40) == register +2:
                screen.append("#")
            else:
                screen.append(" ")

            continue

        cycles += 1
        if int(cycles % 40) == register or int(cycles % 40) == register + 1 or int(cycles % 40) == register + 2:
            screen.append("#")
        else:
            screen.append(" ")

        cycles += 1
        if int(cycles % 40) == register or int(cycles % 40) == register + 1 or int(cycles % 40) == register + 2:
            screen.append("#")
        else:
            screen.append(" ")

        register += int(inp[1])




    except Exception:
        pass





#for i in sigs:
#    if i //


for j in range(6):
    temp = []
    for i in range(40):
        temp.append(screen[(40 * j ) + i])
    print(temp)


