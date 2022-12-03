values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

inp = ""
bag = ["", "", ""]
temp = []
score = 0
c = 0

while True:

    try:


        inp = input()



        if inp == "":
            break


        bag[c] = inp
        c += 1
        c %= 3


        if c == 0:

            temp = []
            for i1 in bag[0]:
                if i1 in bag[1]:
                    temp += i1


            for i2 in bag[2]:
                if i2 in temp:
                    score += values.index(i2) + 1
                    break

            bag = ["", "", ""]




    except Exception:
        pass


print(score)
