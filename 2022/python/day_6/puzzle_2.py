
inp = []
four = []
count = 0



inp = input()



for c in inp:

    count += 1

    if len(four) < 14:
        four = [c] + four
        continue


    # free up first char
    for n in range(13):
        four[13 - n] = four[12 - n]


    four[0] = c


    test = True
    for c2 in four:
        if four.count(c2) > 1:
            test = False


    if test:
        print(count)
        break



