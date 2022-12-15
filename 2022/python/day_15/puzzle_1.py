inp = """Sensor at x=1259754, y=1927417: closest beacon is at x=1174860, y=2000000
Sensor at x=698360, y=2921616: closest beacon is at x=1174860, y=2000000
Sensor at x=2800141, y=2204995: closest beacon is at x=3151616, y=2593677
Sensor at x=3257632, y=2621890: closest beacon is at x=3336432, y=2638865
Sensor at x=3162013, y=3094407: closest beacon is at x=3151616, y=2593677
Sensor at x=748228, y=577603: closest beacon is at x=849414, y=-938539
Sensor at x=3624150, y=2952930: closest beacon is at x=3336432, y=2638865
Sensor at x=2961687, y=2430611: closest beacon is at x=3151616, y=2593677
Sensor at x=142293, y=3387807: closest beacon is at x=45169, y=4226343
Sensor at x=3309479, y=1598941: closest beacon is at x=3336432, y=2638865
Sensor at x=1978235, y=3427616: closest beacon is at x=2381454, y=3683743
Sensor at x=23389, y=1732536: closest beacon is at x=1174860, y=2000000
Sensor at x=1223696, y=3954547: closest beacon is at x=2381454, y=3683743
Sensor at x=3827517, y=3561118: closest beacon is at x=4094575, y=3915146
Sensor at x=3027894, y=3644321: closest beacon is at x=2381454, y=3683743
Sensor at x=3523333, y=3939956: closest beacon is at x=4094575, y=3915146
Sensor at x=2661743, y=3988507: closest beacon is at x=2381454, y=3683743
Sensor at x=2352285, y=2877820: closest beacon is at x=2381454, y=3683743
Sensor at x=3214853, y=2572272: closest beacon is at x=3151616, y=2593677
Sensor at x=3956852, y=2504216: closest beacon is at x=3336432, y=2638865
Sensor at x=219724, y=3957089: closest beacon is at x=45169, y=4226343
Sensor at x=1258233, y=2697879: closest beacon is at x=1174860, y=2000000
Sensor at x=3091374, y=215069: closest beacon is at x=4240570, y=610698
Sensor at x=3861053, y=889064: closest beacon is at x=4240570, y=610698
Sensor at x=2085035, y=1733247: closest beacon is at x=1174860, y=2000000
"""


inp2 = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


arr = []
inp = inp.splitlines()

_2mil = []


for i in inp:
    if i == "":
        break

    print(i)

    line = []
    temp = []

    temp.append(int(i.split(" ")[2][2:-1]))
    temp.append(int(i.split(" ")[3][2:-1]))

    line.append(temp)

    temp = []

    temp.append(int(i.split(" ")[8][2:-1]))
    temp.append(int(i.split(" ")[9][2:]))

    line.append(temp)

    arr.append(line)


print(arr)



for a in arr:
    dist = 0
    dist += abs(a[0][0] - a[1][0])
    dist += abs(a[0][1] - a[1][1])
    print(a, dist)

    dist -= abs(2000000 - a[0][1])

    if dist < 0: continue

    _2mil.append([a[0][0] - dist, a[0][0] + dist])

print("made dist map")

for i in _2mil:
    print(i)

print(" now solving. ")


moves = True



while True:

    if len(_2mil) == 1:
        print("yay", _2mil)
        print("moves", moves)
    temp = []

    if not moves:
        break
    moves = False

    for i in range(len(_2mil)):
        for j in range(i + 1, len(_2mil)):

            if _2mil[i] == _2mil[j]: continue

            min_i = min(_2mil[i])
            max_i = max(_2mil[i])

            min_j = min(_2mil[j])
            max_j = max(_2mil[j])

            if max_j < min_i:
                continue

            if max_i < min_j:
                continue



            if not [min(min_i, min_j), max(max_i, max_j)] in temp:
                temp.append([min(min_i, min_j), max(max_i, max_j)])
                moves = True
                continue

        print(temp)



    if len(temp) == 1:
        print(_2mil)
        print(temp)
    if moves:
        _2mil = temp


print("loop done")
print(_2mil)

init = 0
for n in _2mil:
    init += abs(n[0] - n[1]) + 1

removed = []

for i in arr:
    if i[1][1] == 2000000:
        if not i[1][0] in removed:
            init -= 1
            removed.append(i[1][0])

print(init)