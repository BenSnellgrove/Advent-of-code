values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

inp = ""
score = 0

while True:

    try:

        inp = input()

        if inp == "":
            break


        n = int(len(inp) / 2)
        inp = [inp[0:n], inp[n:]]

        for i in inp[0]:
            if i in inp[1]:

                score += values.index(i) + 1
                break



    except Exception:
        pass


print(score)
