inp = ""

sigs = []

cycles = 1
register = 1

while True:

    try:

        inp = input()

        if inp == "":
            break

        inp = inp.split(" ")

        if len(inp) == 1:
            sigs.append(register)
            # cycles += 1
            continue

        sigs.append(register)
        sigs.append(register)
        register += int(inp[1])









    except Exception:
        pass

print(sigs[19] * 20)
print(sigs[59] * 60)
print(sigs[99] * 100)
print(sigs[139] * 140)
print(sigs[179] * 180)
print(sigs[219] * 220)

print((sigs[19] * 20) + (sigs[59] * 60) + (sigs[99] * 100)+  (sigs[139] * 140)+(sigs[179] * 180)+(sigs[219] * 220)
      )
