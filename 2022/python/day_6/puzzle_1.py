
inp = []
four = []
count = 0



inp = input()



for c in inp:

    count += 1

    if len(four) < 4:
        four = [c] + four
        continue


    # free up first char
    for n in range(3):
        four[3 - n] = four[2 - n]


    four[0] = c


    test = True
    for c2 in four:
        if four.count(c2) > 1:
            test = False


    if test:
        print(count)
        break



