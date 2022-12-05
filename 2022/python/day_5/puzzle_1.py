# hard coded initial state
"""
[N]             [R]             [C]
[T] [J]         [S] [J]         [N]
[B] [Z]     [H] [M] [Z]         [D]
[S] [P]     [G] [L] [H] [Z]     [T]
[Q] [D]     [F] [D] [V] [L] [S] [M]
[H] [F] [V] [J] [C] [W] [P] [W] [L]
[G] [S] [H] [Z] [Z] [T] [F] [V] [H]
[R] [H] [Z] [M] [T] [M] [T] [Q] [W]
 1   2   3   4   5   6   7   8   9
"""



crates = [
    ["R", "G", "H", "Q", "S", "B", "T", "N"],
    ["H", "S", "F", "D", "P", "Z", "J"],
    ["Z", "H", "V"],
    ["M", "Z", "J", "F", "G", "H"],
    ["T", "Z", "C", "D", "L", "M", "S", "R"],
    ["M", "T", "W", "V", "H", "Z", "J"],
    ["T", "F", "P", "L", "Z"],
    ["Q", "V", "W", "S"],
    ["W", "H", "L", "M", "T", "D", "N", "C"],

]
inp = []
temp = []
count = 0

while True:


    inp = input()

    if inp == "":
        break

    inp = inp.split(" ")

    temp = inp
    inp = []
    inp.append(int(temp[1]))
    inp.append(int(temp[3]) - 1)    # because the crates are 1-indexed
    inp.append(int(temp[5]) - 1)

    print(inp)



    for i in range(inp[0]):
        crates[inp[2]].append(crates[inp[1]][-1])
        crates[inp[1]].pop()

    for c in crates:
        print(c)








for c in crates:
    print(c[-1], end="")

print()
